<script lang="ts" generics="Metadata = any">
	import type { Crumb, ModuleData } from '.././types';
	import { onMount } from 'svelte';

	// Relative path to the routes folder for the glob import
	export let relPathToRoutes: string = '/src/routes/';
	// The route from the routers perspective, e.g. $page.route.id
	export let routeId: string | null;
	export let url: URL;
	export let crumbs: Crumb<Metadata>[] | undefined = undefined;
	export function titleSanitizer(title: string) {
		return title.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
	}
	export let routeModules: Record<string, ModuleData> | undefined = undefined;
	export let pageData: any;

	onMount(async () => {
		// If nothing is passed to routeModules, populate it
		if (routeModules === undefined) {
			routeModules = import.meta.glob('/src/routes/**/*.svelte', {
				eager: true
			});
		}
	});

	// Given a module and a crumb, determine the page title
	function getPageTitleFromModule(module: ModuleData | undefined) {
		if (module?.pageTitle) {
			return module.pageTitle;
		}
		// Fall back to crumb title if the function returns undefined
		if (module?.getPageTitle) {
			return module.getPageTitle(pageData);
		}
		return undefined;
	}

	let _crumbs = [] as Crumb<Metadata>[];
	$: {
		_crumbs = [] as Crumb<Metadata>[];
		if (crumbs != undefined) {
			// If crumbs array is passed in always use that with highest priority
			_crumbs = [...crumbs];
		} else if (routeId) {
			// If there is routeing info, use it to find the page modules and
			// subsequently the page titles for each route leading up to the
			// current page.
			let completeUrl = '';
			let completeRoute = relPathToRoutes + (relPathToRoutes.slice(-1) == '/' ? '' : '/');
			// Split the route ID on every forward slash, but if there is a group route include that in the
			// following route. This accounts for the fact that (group) routes do not show up in the path.
			// For Example:
			// routeId: test/(group1)/test2/test3
			// routes: ["test", "(group1)/test2", "test3"]
			const routes = routeId.split(/(?<!\))\//).filter((p) => p != '');
			const paths = url.pathname.split('/').filter((p) => p != '');

			// Loop over each directory in the path and generate a crumb
			// for each one.
			for (let i = 0; i < paths.length; i++) {
				let path = paths[i];
				let route = routes[i];
				completeUrl += `/${path}`;

				// Note: the slash is trailing here because the prefix always exists as the provided
				// relative path to the routes folder, and we are appending another path to
				// the end later
				completeRoute += `${route}/`;

				// routeModules type is technically undefined so we can detect when a value
				// is passed in or not, but will always be generated in the onMount as a
				// fallback.
				const routeModule =
					routeModules === undefined ? undefined : routeModules[`${completeRoute}+page.svelte`];

				_crumbs.push({
					// Last crumb gets no url as it is the current page
					url: i == paths.length - 1 ? undefined : completeUrl,
					title: getPageTitleFromModule(routeModule) || titleSanitizer(path)
				});
			}

			// Force trigger an update
			_crumbs = _crumbs;
		} else {
			// And if there is no route info, simply generate breadcrumbs from the url
			// path
			let completeUrl = '';
			const paths = url.pathname.split('/').filter((p) => p != '');
			for (let i = 0; i < paths.length; i++) {
				let path = paths[i];
				completeUrl += `/${path}`;
				_crumbs.push({
					title: titleSanitizer(path),
					url: i == paths.length - 1 ? undefined : completeUrl
				});
			}

			_crumbs = _crumbs;
		}
	}
</script>

<slot crumbs={_crumbs} {routeModules} />
