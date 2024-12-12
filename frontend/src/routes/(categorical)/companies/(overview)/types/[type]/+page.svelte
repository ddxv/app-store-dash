<script lang="ts">
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
	import CompaniesTableGrid from '$lib/CompaniesTableGrid.svelte';

	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

{#await data.companiesOverview}
	<div><span>Loading...</span></div>
{:then tableData}
	{#if typeof tableData == 'string'}
		Failed to load companies.
	{:else if tableData.categories}
		<CompaniesTableGrid>
			{#snippet mainTable()}
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			{/snippet}
			{#snippet sdkAndroidTotalApps()}
				<span
					>Android Companies:
					{formatNumber(tableData.categories.categories.all.sdk_android_total_companies)}
				</span>
			{/snippet}
			{#snippet sdkIosTotalApps()}
				<span
					>iOS Companies: {formatNumber(
						tableData.categories.categories.all.sdk_ios_total_companies
					)}</span
				>
			{/snippet}
			{#snippet adstxtAndroidTotalApps()}
				<span
					>Android Companies: {formatNumber(
						tableData.categories.categories.all.adstxt_direct_android_total_companies
					)}</span
				>
			{/snippet}
			{#snippet adstxtIosTotalApps()}
				<span
					>iOS Companies: {formatNumber(
						tableData.categories.categories.all.adstxt_direct_ios_total_companies
					)}</span
				>
			{/snippet}
		</CompaniesTableGrid>
	{/if}
{/await}
