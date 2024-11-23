<script lang="ts">
	import { page } from '$app/stores';
	import CompaniesBarChart from '$lib/CompaniesBarChart.svelte';
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';

	import WhiteCard from '$lib/WhiteCard.svelte';
	import CompaniesLayout from '$lib/CompaniesLayout.svelte';
	import CompaniesTableGrid from '$lib/CompaniesTableGrid.svelte';

	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	let currentCategoryName = $derived(getCategoryName($page.params.category));

	function getCategoryName(category: string) {
		return (
			data?.appCats?.categories?.find((cat: { id: string }) => cat.id == category)?.name || category
		);
	}

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<div class="flex items-center mb-2">
	<h1 class="h1 text-3xl font-bold text-primary-900-100">Companies in {currentCategoryName}</h1>
</div>

{#await data.companiesOverview}
	<div class="card preset-tonal p-6 rounded-lg shadow-md flex justify-center items-center h-40">
		<span class="text-lg">Loading...</span>
	</div>
{:then myData}
	{#if typeof myData == 'string'}
		<p class="text-red-500 text-center">Failed to load company details.</p>
	{:else if myData.categories.categories.companies}
		<CompaniesLayout>
			{#snippet card1()}
				<WhiteCard>
					<div class="p-6 rounded-lg shadow-md">
						<h2 class="text-xl font-bold text-primary-900-100 mb-4">Total Companies</h2>
						<p class="text-lg">
							<span class="font-semibold text-primary-900-100"
								>{formatNumber(myData.categories.categories.companies.total_companies)}</span
							>
						</p>
					</div>
				</WhiteCard>
			{/snippet}

			{#snippet card2()}
				<WhiteCard>
					{#snippet title()}
						Top SDK Companies
					{/snippet}
					<CompaniesBarChart plotData={myData.top.sdk} />
				</WhiteCard>
			{/snippet}
			{#snippet card3()}
				<WhiteCard>
					{#snippet title()}
						Top Adstxt Companies
					{/snippet}
					<CompaniesBarChart plotData={myData.top.adstxt_direct} />
				</WhiteCard>
			{/snippet}
		</CompaniesLayout>
	{/if}
{:catch error}
	<p class="text-red-500 text-center">{error.message}</p>
{/await}

{#await data.companiesOverview}
	<div><span>Loading...</span></div>
{:then tableData}
	{#if typeof tableData == 'string'}
		Failed to load companies.
	{:else if tableData.categories.categories}
		<CompaniesTableGrid>
			{#snippet mainTable()}
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			{/snippet}

			{#snippet sdkAndroidTotalApps()}
				Android Companies: {formatNumber(
					tableData.categories.categories.companies.sdk_android_total_companies
				)}
			{/snippet}
			{#snippet sdkIosTotalApps()}
				iOS Companies: {formatNumber(
					tableData.categories.categories.companies.sdk_ios_total_companies
				)}
			{/snippet}
			{#snippet adstxtAndroidTotalApps()}
				Android Companies:
				{formatNumber(
					tableData.categories.categories.companies.adstxt_direct_android_total_companies
				)}
			{/snippet}
			{#snippet adstxtIosTotalApps()}
				iOS Companies: {formatNumber(
					tableData.categories.categories.companies.adstxt_direct_ios_total_companies
				)}
			{/snippet}
		</CompaniesTableGrid>
	{:else}
		<p>categegories.all is missing!</p>
	{/if}
{/await}
