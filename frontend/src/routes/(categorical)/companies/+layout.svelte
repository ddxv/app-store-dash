<script lang="ts">
	import { page } from '$app/stores';
	import type { Crumb } from '../../../types';
	import Breadcrumbs from '$lib/Breadcrumbs.svelte';
	import CompanyTypesTabs from '$lib/utils/CompanyTypesTabs.svelte';
	import type { MyCrumbMetadata } from '../../../types';

	import type { CompanyTypes } from '../../../types';

	// interface Props {
	// 	data: CompaniesLayoutResponse;
	// 	children?: import('svelte').Snippet;
	// }

	let { data, children } = $props();

	let companyTypes = $page.data.companyTypes;
	// let appCats = $page.data.appCats;

	let pageDataCrumbs = $derived($page.data.crumbs as Crumb<MyCrumbMetadata>[] | undefined);

	// let rel_link = $state('');

	let type_title: string = $derived(getTypeTitle(companyTypes, $page.params.type));
	let category_title = $derived(getCategoryName($page.params.category));

	function getTypeTitle(myTypes: CompanyTypes, currentType: string) {
		if (myTypes.types && currentType) {
			return myTypes.types.find((type: { url_slug: string }) => type.url_slug === currentType).name;
		}
		return '';
	}

	function getCategoryName(category: string) {
		if (category) {
			return (
				data?.appCats?.categories?.find((cat: { id: string }) => cat.id == category)?.name ||
				category
			);
		}
		return '';
	}

	// if ($page.params.type) {
	// 	// type_title = companyTypes.types[type].name;
	// 	if (!$page.params.category) {
	// 		// page is /companies/types/[type]
	// 		rel_link = `types/${$page.params.type}`;
	// 	} else if ($page.params.category) {
	// 		// page is /companies/types/[type]/[category]
	// 		rel_link = `types/${$page.params.type}/${$page.params.category}`;
	// 	}
	// } else if ($page.params.category) {
	// 	// page is /companies/categores/[category]
	// 	rel_link = `categories/${$page.params.category}`;
	// } else {
	// 	// page is /companies
	// 	rel_link = '';
	// }

	let title = $derived(`${type_title} ${category_title} Top Companies | AppGoblin`);
	let description = $derived(
		`Explore ${type_title} ${category_title} biggest companies and user bases. Explore detailed analytics, market presence, and insights about ${type_title}'s role in the mobile ecosystem.`
	);
	let keywords = $derived(
		`${type_title}, ${category_title}, android, ios, adtech, advertising network, data tracking, mobile measurement, programmatic advertising, app-ads.txt, mobile advertising, ad tech analytics, AppGoblin`
	);
</script>

<svelte:head>
	<title>{title}</title>
	<link rel="canonical" href={$page.url.href} />
	<meta name="description" content={description} />
	<meta name="keywords" content={keywords} />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={description} />

	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content={$page.url.href} />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
</svelte:head>

<div class="text-surface-900-100 text-sm p-2 md:p-4">
	<Breadcrumbs
		url={$page.url}
		routeId={$page.route.id}
		pageData={$page.data}
		crumbs={pageDataCrumbs}
	>
		{#snippet children({ crumbs })}
			<div>
				<span><a href="/" class="text-surface-900-100 hover:text-primary-900-100">Home</a></span>
				{#each crumbs as c}
					<span>/</span>
					<span>
						{#if c.title != 'Types' && c.title != 'Categories'}
							<a href={c.url} class="text-surface-900-100 hover:text-primary-900-100">
								{c.title}
								{c.metadata ? `(${c.metadata.extraValue})` : ''}
							</a>
						{:else}
							{c.title}
							{c.metadata ? `(${c.metadata.extraValue})` : ''}
						{/if}
					</span>
				{/each}
			</div>
		{/snippet}
	</Breadcrumbs>
</div>

{#await data.companyTypes}
	Loading company types ...
{:then myTabs}
	{#if myTabs && myTabs.types.length > 0}
		<CompanyTypesTabs {myTabs} />
	{/if}
{/await}

<div class="card-content p-1 md:p-6 shadow-md rounded-lg">
	{@render children?.()}
</div>
