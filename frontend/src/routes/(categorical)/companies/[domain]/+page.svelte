<script lang="ts">
	import type { CompanyFullDetails } from '../../../../types';

	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';
	import CompanyCategoryPie from '$lib/CompanyCategoryPie.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
	import CompanyTree from '$lib/CompanyTree.svelte';
	import CompanySDKs from '$lib/CompanySDKs.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';
	import CompaniesLayout from '../../../../lib/CompaniesLayout.svelte';
	interface Props {
		data: CompanyFullDetails;
	}

	let { data }: Props = $props();
	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<CompaniesLayout>
	{#snippet card1()}
		<WhiteCard>
			{#await data.companyParentCategories}
				<span class="text-lg">Loading...</span>
			{:then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else if myData && myData.length > 0}
					<div class=" p-2 rounded-lg shadow-md">
						<h2 class="text-xl font-bold text-primary-900-100 mb-4">Total Apps</h2>
						<p class="text-lg">
							<span class="font-semibold text-primary-900-100"
								>{formatNumber(myData.map((d) => d.value).reduce((a, b) => a + b, 0))}</span
							>
						</p>
					</div>
				{/if}
			{:catch error}
				<p class="text-red-500 text-center">{error.message}</p>
			{/await}
		</WhiteCard>
	{/snippet}

	{#snippet card2()}
		<WhiteCard>
			<div>
				{#await data.companyParentCategories}
					<span class="text-lg">Loading...</span>
				{:then myPieData}
					{#if typeof myPieData == 'string'}
						<p class="text-red-500 text-center">Failed to load parent categories.</p>
					{:else if myPieData}
						<CompanyCategoryPie plotData={myPieData} />
					{/if}
				{:catch error}
					<p class="text-red-500 text-center">{error.message}</p>
				{/await}
			</div>
		</WhiteCard>
	{/snippet}

	{#snippet card3()}
		<WhiteCard>
			{#snippet title()}
				<span>Subsidiary Companies</span>
			{/snippet}
			{#await data.companyTree}
				<span class="text-lg">Loading...</span>
			{:then myTree}
				{#if typeof myTree == 'string'}
					<p class="text-red-500 text-center">Failed to load company tree.</p>
				{:else if myTree && myTree.children_companies.length > 0}
					<CompanyTree {myTree} />
				{:else}
					<!-- Render nothing if there are no child companies -->
				{/if}
			{:catch error}
				<p class="text-red-500 text-center">{error.message}</p>
			{/await}
		</WhiteCard>
	{/snippet}

	{#snippet card4()}
		<WhiteCard>
			{#snippet title()}
				<span>Company SDKs</span>
			{/snippet}
			{#await data.companySdks}
				<span class="text-lg">Loading...</span>
			{:then mySdks}
				{#if typeof mySdks == 'string'}
					<p class="text-red-500 text-center">Failed to load company SDKs.</p>
				{:else if mySdks}
					<CompanySDKs {mySdks} />
				{/if}
			{/await}
		</WhiteCard>
	{/snippet}
</CompaniesLayout>

{#await data.companyDetails}
	<div><span>Loading...</span></div>
{:then detailsData}
	{#await data.companyTopApps}
		<div><span>Loading...</span></div>
	{:then tableData}
		{#if typeof tableData == 'string'}
			Failed to load company's apps.
		{:else}
			<CompanyTableGrid>
				{#snippet sdkAndroidTotalApps()}
					Total Android Apps: {formatNumber(detailsData.categories.all.sdk_android_total_apps)}
				{/snippet}
				{#snippet sdkIosTotalApps()}
					Total iOS Apps: {formatNumber(detailsData.categories.all.sdk_ios_total_apps)}
				{/snippet}
				{#snippet adstxtAndroidTotalApps()}
					Total Android Apps: {formatNumber(
						detailsData.categories.all.adstxt_direct_android_total_apps
					)}
				{/snippet}
				{#snippet adstxtIosTotalApps()}
					Total iOS Apps: {formatNumber(detailsData.categories.all.adstxt_direct_ios_total_apps)}
				{/snippet}

				{#snippet sdkAndroid()}
					{#if tableData && tableData.sdk.android.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
					{/if}
				{/snippet}
				{#snippet sdkIos()}
					{#if tableData && tableData.sdk.ios.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
					{/if}
				{/snippet}
				{#snippet adstxtAndroid()}
					{#if tableData && tableData.adstxt_direct.android.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.android.apps} />
					{/if}
				{/snippet}
				{#snippet adstxtIos()}
					{#if tableData && tableData.adstxt_direct.ios.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.ios.apps} />
					{/if}
				{/snippet}
			</CompanyTableGrid>
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
{/await}
