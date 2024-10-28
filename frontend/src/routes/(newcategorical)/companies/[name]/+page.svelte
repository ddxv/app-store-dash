<script lang="ts">
	import type { CompanyFullDetails } from '../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
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
				{#each myTree.domains as domain}
					<ExternalLink {domain} />
				{/each}
			</div>
		{/if}
	{:catch error}
		<p class="text-red-500">{error.message}</p>
	{/await}
</div>

{#await data.companyTree then myTree}
	{#if myTree && myTree.parent_company_name && myTree.parent_company_domain}
		<div class="flex items-center mt-2 ml-4">
			<p class="text-xl font-bold text-gray-800 mr-2">Parent Company:</p>
			<CompanyButton
				companyName={myTree.parent_company_name}
				companyDomain={myTree.parent_company_domain}
			/>
		</div>
	{/if}
{/await}

<CompaniesLayout>
	{#snippet card1()}
		<WhiteCard >
			{#await data.companyDetails}
				<span class="text-lg text-gray-600">Loading...</span>
			{:then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else if myData.categories.all}
					<div class="bg-white p-6 rounded-lg shadow-md">
						<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
						<p class="text-lg text-gray-700">
							<span class="font-semibold text-gray-900"
								>{formatNumber(myData.categories.all.total_apps)}</span
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
		<WhiteCard >
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
		<WhiteCard >
			{#snippet title()}
				<span >Subsidiary Companies</span>
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
		<WhiteCard >
			{#snippet title()}
				<span >Company SDKs</span>
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
				<!-- @migration-task: migrate this slot by hand, `sdk-android-total-apps` is an invalid identifier -->
	<span slot="sdk-android-total-apps">
					Android Apps: {formatNumber(detailsData.categories.all.sdk_android_total_apps)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `sdk-ios-total-apps` is an invalid identifier -->
	<span slot="sdk-ios-total-apps">
					iOS Apps: {formatNumber(detailsData.categories.all.sdk_ios_total_apps)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `adstxt-android-total-apps` is an invalid identifier -->
	<span slot="adstxt-android-total-apps">
					Android Companies: {formatNumber(
						detailsData.categories.all.adstxt_direct_android_total_apps
					)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `adstxt-ios-total-apps` is an invalid identifier -->
	<span slot="adstxt-ios-total-apps">
					iOS Companies: {formatNumber(detailsData.categories.all.adstxt_direct_ios_total_apps)}
				</span>

				<!-- @migration-task: migrate this slot by hand, `sdk-android` is an invalid identifier -->
	<div slot="sdk-android">
					{#if tableData && tableData.sdk.android.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `sdk-ios` is an invalid identifier -->
	<div slot="sdk-ios">
					{#if tableData && tableData.sdk.ios.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `adstxt-android` is an invalid identifier -->
	<div slot="adstxt-android">
					{#if tableData && tableData.adstxt_direct.android.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.android.apps} />
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `adstxt-ios` is an invalid identifier -->
	<div slot="adstxt-ios">
					{#if tableData && tableData.adstxt_direct.ios.apps.length > 0}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.ios.apps} />
					{/if}
				</div>
			</CompanyTableGrid>
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
{/await}
