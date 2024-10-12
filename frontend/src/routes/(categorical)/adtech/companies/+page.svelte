<script lang="ts">
	import type { CompaniesOverview } from '../../../../types';
	export let data: CompaniesOverview;
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
</script>

<div class="flex items-center mb-2">
	<h1 class="text-3xl font-bold text-gray-800">Companies Overview</h1>
	<div class="h-8 w-px bg-gray-300 mx-2"></div>
</div>

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<div class="bg-white p-6 rounded-lg shadow-md">
		<div class="lg:col-span-1">
			{#await data.companiesOverview}
				<div class="bg-white p-6 rounded-lg shadow-md flex justify-center items-center h-40">
					<span class="text-lg text-gray-600">Loading...</span>
				</div>
			{:then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
					<!-- {:else if myData.categories.all}
					<div class="bg-white p-6 rounded-lg shadow-md">
						<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
						<p class="text-lg text-gray-700">
							<span class="font-semibold text-gray-900"
								>{formatNumber(myData.categories.all.total_apps)}</span
							>
						</p>
					</div> -->
				{/if}
			{:catch error}
				<p class="text-red-500 text-center">{error.message}</p>
			{/await}
		</div>
	</div>

	CHART HERE

	<div class="lg:col-span-3">SOMETHING HERE?</div>
</div>
{#await data.companiesOverview}
	<div><span>Loading...</span></div>
{:then tableData}
	{#if typeof tableData == 'string'}
		Failed to load companies.
	{:else}
		<CompanyTableGrid>
			<!-- <span slot="sdk-android-total-apps">
			{formatNumber(myData.categories.all.sdk_android_total_apps)}
		</span>
		<span slot="sdk-ios-total-apps">
			{formatNumber(myData.categories.all.sdk_ios_total_apps)}
		</span>
		<span slot="adstxt-android-total-apps">
			{formatNumber(myData.categories.all.adstxt_android_total_apps)}
		</span>
		<span slot="adstxt-ios-total-apps">
			{formatNumber(myData.categories.all.adstxt_ios_total_apps)}
		</span> -->

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
