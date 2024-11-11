<script lang="ts">
	import { page } from '$app/stores';
	import type { Crumb } from '../../../types';
	import Breadcrumbs from '$lib/Breadcrumbs.svelte';
	import type { MyCrumbMetadata, CompaniesLayoutResponse } from '../../../types';

	function typeTabClass(tab: string) {
		return $page.url.pathname.startsWith(`/companies/types/${tab}`)
			? 'btn variant-filled-primary'
			: '';
	}

	interface Props {
		data: CompaniesLayoutResponse;
		children?: import('svelte').Snippet;
	}

	let { data, children }: Props = $props();

	let pageDataCrumbs = $derived($page.data.crumbs as Crumb<MyCrumbMetadata>[] | undefined);
</script>

<Breadcrumbs url={$page.url} routeId={$page.route.id} pageData={$page.data} crumbs={pageDataCrumbs}>
	{#snippet children({ crumbs })}
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
	{/snippet}
</Breadcrumbs>

{#await data.companyTypes}
	Loading company types ...
{:then myTabs}
	{#if myTabs && myTabs.types.length > 0}
		<div class="flex flex-row">
			<a href="/companies" class={typeTabClass('all')}>All</a>
			{#each myTabs.types as tab}
				<a href="/companies/types/{tab.url_slug}" class={typeTabClass(tab.url_slug)}>{tab.name}</a>
			{/each}
		</div>
	{/if}
{/await}

<div class="card-content p-1 md:p-6 bg-white shadow-md rounded-lg mt-2">
	{@render children?.()}
</div>
