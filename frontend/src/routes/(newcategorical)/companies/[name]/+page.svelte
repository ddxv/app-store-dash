<script lang="ts">
	import type { CompanyFullDetails } from '../../../../types';
	import { page } from '$app/stores';

	let name = $derived($page.params.name);

	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';
	import CompanyCategoryPie from '$lib/CompanyCategoryPie.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
	import CompanyTree from '$lib/CompanyTree.svelte';
	import CompanySDKs from '$lib/CompanySDKs.svelte';
	import ExternalLink from '$lib/ExternalLink.svelte';
	import CompanyButton from '$lib/CompanyButton.svelte';
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

<div class="flex items-center mb-2">
	<h1 class="text-3xl font-bold text-gray-800">{name}</h1>
	<div class="h-8 w-px bg-gray-300 mx-2"></div>
	{#await data.companyTree}
		<span class="text-lg text-gray-600">Loading...</span>
	{:then myTree}
		{#if typeof myTree == 'string'}
			<p class="text-red-500">Failed to load company tree.</p>
		{:else if myTree}
			<div class="flex items-center">
				{#if myTree.queried_company_domain}
					{#if myTree.parent_company_domain == myTree.queried_company_domain}
						<!-- IS PARENT COMPANY -->
						<h2 class="text-xl font-bold text-gray-800 mr-2">{myTree.parent_company_name}</h2>
						<div class="h-8 w-px bg-gray-300 mx-2"></div>
						<ExternalLink domain={myTree.parent_company_domain} />
					{:else}
						<h2 class="text-xl font-bold text-gray-800 mr-2">{myTree.queried_company_name}</h2>
						<div class="h-8 w-px bg-gray-300 mx-2"></div>
						<ExternalLink domain={myTree.queried_company_domain} />
						<div class="h-8 w-px bg-gray-300 mx-2"></div>
						<!-- HAS PARENT COMPANY -->
						<!-- <h2 class="text-xl font-bold text-gray-800 mr-2">PARENT: {myTree.queried_company_domain} {myTree.parent_company_name} AA</h2> -->
						<h2 class="h2 text-xl font-bold text-gray-800 mr-2">Parent Company:</h2>
						<CompanyButton
							companyName={myTree.parent_company_name}
							companyDomain={myTree.parent_company_domain}
						/>
					{/if}
				{/if}
			</div>
		{/if}
	{:catch error}
		<p class="text-red-500">{error.message}</p>
	{/await}
</div>

<CompaniesLayout>
	{#snippet card1()}
		<WhiteCard>
			{#await data.companyParentCategories}
				<span class="text-lg text-gray-600">Loading...</span>
			{:then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else if myData && myData.length > 0}
					<div class="bg-white p-2 rounded-lg shadow-md">
						<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
						<p class="text-lg text-gray-700">
							<span class="font-semibold text-gray-900"
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
					<span class="text-lg text-gray-600">Loading...</span>
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
				<span class="text-lg text-gray-600">Loading...</span>
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
				<span class="text-lg text-gray-600">Loading...</span>
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
					{name} total Android apps: {formatNumber(
						detailsData.categories.all.sdk_android_total_apps
					)}
				{/snippet}
				{#snippet sdkIosTotalApps()}
					{name} total iOS apps: {formatNumber(detailsData.categories.all.sdk_ios_total_apps)}
				{/snippet}
				{#snippet adstxtAndroidTotalApps()}
					{name} total Android apps: {formatNumber(
						detailsData.categories.all.adstxt_direct_android_total_apps
					)}
				{/snippet}
				{#snippet adstxtIosTotalApps()}
					{name} total iOS apps: {formatNumber(
						detailsData.categories.all.adstxt_direct_ios_total_apps
					)}
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
