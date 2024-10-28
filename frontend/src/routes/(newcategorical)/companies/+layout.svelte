<script lang="ts">
	import { page } from '$app/stores';
	import type { Crumb } from '../../../types';
	import Breadcrumbs from '$lib/Breadcrumbs.svelte';
	import type { MyCrumbMetadata, CompaniesLayoutResponse } from '../../../types';
	import CompanyTypesTabs from '$lib/utils/CompanyTypesTabs.svelte';

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
		<CompanyTypesTabs myTabs={myTabs.types}></CompanyTypesTabs>
	{/if}
{/await}

<div class="card-content p-6 bg-white shadow-md rounded-lg mt-2">
	{@render children?.()}
</div>
