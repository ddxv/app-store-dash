<script lang="ts">
	import type { CompaniesOverview } from '../../../types';
	export let data: CompaniesOverview;
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
	import CompaniesBarChart from '$lib/CompaniesBarChart.svelte';
	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';
	import CompaniesLayout from '$lib/CompaniesLayout.svelte';

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<svelte:head>
	<title>Top Adtech Companies, Ad Networks & Data Trackers | AppGoblin</title>
	<meta
		name="description"
		content="Explore top-ranked adtech advertising networks, data trackers, MMPs, and programmatic networks. Discover insights from app-ads.txt files and our extensive research on hundreds of ad tech companies across various app categories."
	/>
	<meta
		name="keywords"
		content="adtech companies, advertising networks, data trackers, MMPs, programmatic networks, app-ads.txt, mobile advertising, ad tech analytics, app marketing, AppGoblin"
	/>
	<meta property="og:title" content="Top Adtech Companies & Ad Networks | AppGoblin Analytics" />
	<meta
		property="og:description"
		content="Discover top adtech companies, ad networks, and data trackers. Explore comprehensive data on hundreds of ad tech firms, their app clients, and market presence across different app categories."
	/>
	<meta name="twitter:title" content="Leading Adtech Companies & Networks | AppGoblin Insights" />
	<meta
		name="twitter:description"
		content="Uncover insights on top adtech firms, ad networks, and data trackers. Analyze data from app-ads.txt files and our research on hundreds of ad tech companies and their app clients."
	/>
	<meta property="og:image" content="https://appgoblin.info/adtech-companies-banner.png" />
	<meta property="og:url" content="https://appgoblin.info/companies" />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://appgoblin.info/adtech-companies-banner.png" />
	<link rel="canonical" href="https://appgoblin.info/companies" />
</svelte:head>

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
	{:else if myData && myData.categories}
		<CompaniesLayout>
			<WhiteCard slot="card1">
				<div class="bg-white p-6 rounded-lg shadow-md">
					<h2 class="text-xl font-bold text-gray-800 mb-4">Total Ad Tech Companies</h2>
					<p class="text-lg text-gray-700">
						<span class="font-semibold text-gray-900"
							>{formatNumber(myData.categories.categories.all.total_apps)}</span
						>
					</p>
				</div>
			</WhiteCard>

			<WhiteCard slot="card2"
				><CompaniesBarChart plotData={myData.sdk.top} plotTitle="Top SDK Companies" /></WhiteCard
			>
			<WhiteCard slot="card3"
				><CompaniesBarChart
					plotData={myData.adstxt.top}
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
	{:else if tableData.categories}
		<CompanyTableGrid>
			<span slot="sdk-android-total-apps"
				>Android Companies:
				{formatNumber(tableData.categories.categories.all.sdk_android_total_apps)}
			</span>
			<span slot="sdk-ios-total-apps">
				iOS Companies: {formatNumber(tableData.categories.categories.all.sdk_ios_total_apps)}
			</span>
			<span slot="adstxt-android-total-apps">
				Android Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_android_total_apps
				)}
			</span>
			<span slot="adstxt-ios-total-apps">
				iOS Companies: {formatNumber(tableData.categories.categories.all.adstxt_ios_total_apps)}
			</span>

			<div slot="sdk-android">
				{#if tableData && tableData.sdk.android.length > 0}
					<CompaniesOverviewTable entries_table={tableData.sdk.android} />
				{/if}
			</div>
			<div slot="sdk-ios">
				{#if tableData && tableData.sdk.ios.length > 0}
					<CompaniesOverviewTable entries_table={tableData.sdk.ios} />
				{/if}
			</div>
			<div slot="adstxt-android">
				{#if tableData && tableData.adstxt.android.length > 0}
					<CompaniesOverviewTable entries_table={tableData.adstxt.android} />
				{/if}
			</div>
			<div slot="adstxt-ios">
				{#if tableData && tableData.adstxt.ios.length > 0}
					<CompaniesOverviewTable entries_table={tableData.adstxt.ios} />
				{/if}
			</div>
		</CompanyTableGrid>
	{/if}
{/await}
