<script lang="ts">
	import type { CompaniesOverview } from '../../../../types';
	export let data: CompaniesOverview;
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
</script>

<div>
	{#await data.companiesOverview}
		<div>
			<span>Loading...</span>
		</div>
	{:then apps}
		{#if typeof apps == 'string'}
			Failed to load network's apps.
		{:else}
			<div class="flex gap-2">
				<div class="card variant-filled">
					<div class="card-header">Top DOGG</div>
					<CompaniesOverviewTable entries_table={apps.sdk.android}></CompaniesOverviewTable>
				</div>
				<CompaniesOverviewTable entries_table={apps.sdk.ios}></CompaniesOverviewTable>
				<p class="p-2" />
				<CompaniesOverviewTable entries_table={apps.adstxt.android}></CompaniesOverviewTable>
				<CompaniesOverviewTable entries_table={apps.adstxt.ios}></CompaniesOverviewTable>
			</div>

			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
