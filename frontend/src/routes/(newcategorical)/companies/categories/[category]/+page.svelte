<script lang="ts">
	import type { CompaniesOverview } from '../../../../../types';
	export let data: CompaniesOverview;
	import CompaniesBarChart from '$lib/CompaniesBarChart.svelte';
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';

	import WhiteCard from '$lib/WhiteCard.svelte';
	import CompaniesLayout from '$lib/CompaniesLayout.svelte';
	import CompaniesTableGrid from '$lib/CompaniesTableGrid.svelte';

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<div class="flex items-center mb-2">
	<h1 class="text-3xl font-bold text-gray-800">Companies Overview</h1>
	<div class="h-8 w-px bg-gray-300 mx-2"></div>
</div>

{#await data.companiesOverview}
	<div class="bg-white p-6 rounded-lg shadow-md flex justify-center items-center h-40">
		<span class="text-lg text-gray-600">Loading...</span>
	</div>
{:then myData}
	{#if typeof myData == 'string'}
		<p class="text-red-500 text-center">Failed to load company details.</p>
	{:else if myData.categories.categories}
		<CompaniesLayout>
			<WhiteCard slot="card1">
				<div class="bg-white p-6 rounded-lg shadow-md">
					<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
					<p class="text-lg text-gray-700">
						<span class="font-semibold text-gray-900"
							>{formatNumber(myData.categories.categories.all.total_apps)}</span
						>
					</p>
				</div>
			</WhiteCard>

			<WhiteCard slot="card2">
				<CompaniesBarChart plotData={myData.sdk.top} plotTitle="Top SDK Companies" />
			</WhiteCard>
			<WhiteCard slot="card3"
				><CompaniesBarChart
					plotData={myData.adstxt_direct.top}
					plotTitle="Top Adstxt Companies"
				/></WhiteCard
			>
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
	{:else}
		<CompaniesTableGrid>
			<div slot="main-table">
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			</div>

			<span slot="sdk-android-total-apps">
				Android Companies: {formatNumber(
					tableData.categories.categories.all.sdk_android_total_apps
				)}
			</span>
			<span slot="sdk-ios-total-apps">
				iOS Companies: {formatNumber(tableData.categories.categories.all.sdk_ios_total_apps)}
			</span>
			<span slot="adstxt-android-total-apps">
				Android Companies:
				{formatNumber(tableData.categories.categories.all.adstxt_direct_android_total_apps)}
			</span>
			<span slot="adstxt-ios-total-apps">
				iOS Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_direct_ios_total_apps
				)}
			</span>
		</CompaniesTableGrid>
	{/if}
{/await}
