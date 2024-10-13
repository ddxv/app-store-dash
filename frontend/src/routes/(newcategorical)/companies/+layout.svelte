<script lang="ts">
	import { page } from '$app/stores';
	import type { Crumb } from '../../../types';
	import Breadcrumbs from '$lib/Breadcrumbs.svelte';
	import type { MyCrumbMetadata } from '../../../types';

	$: pageDataCrumbs = $page.data.crumbs as Crumb<MyCrumbMetadata>[] | undefined;
</script>

<Breadcrumbs
	url={$page.url}
	routeId={$page.route.id}
	pageData={$page.data}
	crumbs={pageDataCrumbs}
	let:crumbs
>
	<div>
		<span><a href="/">Home</a></span>
		{#each crumbs as c}
			<span>/</span>
			<span>
				<a href={c.url}>
					<!-- 
		Pass in the glob import of the route svelte modules as well as
		any data the routes can use to try to fill in any info.
		-->
					{c.title}
					{c.metadata ? `(${c.metadata.extraValue})` : ''}
				</a>
			</span>
		{/each}
	</div>
</Breadcrumbs>
<div class="card-content p-6 bg-white shadow-md rounded-lg mt-2">
	<slot />
</div>
