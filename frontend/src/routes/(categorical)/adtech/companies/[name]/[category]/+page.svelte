<script lang="ts">
	import type { CompanyCategoryDetails } from '../../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	export let data: CompanyCategoryDetails;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';

	import CompaniesLayout from '$lib/CompaniesLayout.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';

	$: company_category = $page.params.category;

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<h1 class="text-3xl font-bold mb-6 text-gray-800">{name}: {company_category}</h1>
<CompaniesLayout>
	<WhiteCard slot="card1">
		{#await data.companyDetails}
			<div class="bg-white p-6 rounded-lg shadow-md flex justify-center items-center h-40">
				<span class="text-lg text-gray-600">Loading...</span>
			</div>
		{:then myData}
			{#if typeof myData == 'string'}
				<p class="text-red-500 text-center">Failed to load company details.</p>
			{:else if myData}
				<div class="bg-white p-6 rounded-lg shadow-md">
					<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
					<p class="text-lg text-gray-700">
						<span class="font-semibold text-gray-900"
							>{formatNumber(myData.categories[company_category].total_apps)}</span
						>
					</p>
				</div>
			{/if}
		{:catch error}
			<p class="text-red-500 text-center">{error.message}</p>
		{/await}
	</WhiteCard>
</CompaniesLayout>

{#await data.companyDetails}
	<div><span>Loading...</span></div>
{:then myData}
	<CompanyTableGrid>
		<span slot="sdk-android-total-apps">
			{formatNumber(myData.categories[company_category].sdk_android_total_apps)}
		</span>
		<span slot="sdk-ios-total-apps">
			{formatNumber(myData.categories[company_category].sdk_ios_total_apps)}
		</span>
		<span slot="adstxt-android-total-apps">
			{formatNumber(myData.categories[company_category].adstxt_android_total_apps)}
		</span>
		<span slot="adstxt-ios-total-apps">
			{formatNumber(myData.categories[company_category].adstxt_ios_total_apps)}
		</span>

		<div slot="sdk-android">
			{#await data.companyCategoryApps}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData.sdk.android.apps}
					<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
				{:else}
					Failed to load company overview.
				{/if}
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}
		</div>
		<div slot="sdk-ios">
			{#await data.companyCategoryApps}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData.sdk.ios.apps}
					<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
				{/if}
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}
		</div>
		<div slot="adstxt-android">
			{#await data.companyCategoryApps}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData.adstxt.android.apps}
					<CompanyOverviewTable entries_table={tableData.adstxt.android.apps} />
				{/if}
			{/await}
		</div>
		<div slot="adstxt-ios">
			{#await data.companyCategoryApps}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData.adstxt.ios.apps}
					<CompanyOverviewTable entries_table={tableData.adstxt.ios.apps} />
				{/if}
			{/await}
		</div>
	</CompanyTableGrid>
{/await}
