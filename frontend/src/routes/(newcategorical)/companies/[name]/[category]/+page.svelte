<script lang="ts">
	import type { CompanyCategoryDetails } from '../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';

	import CompaniesLayout from '$lib/CompaniesLayout.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
	import ExternalLink from '$lib/ExternalLink.svelte';
	import CompanyButton from '$lib/CompanyButton.svelte';
	interface Props {
		data: CompanyCategoryDetails;
	}

	let { data }: Props = $props();

	let company_category = $derived($page.params.category);

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

<h3 class="text-xl font-bold mb-6 text-gray-800">Category: {company_category}</h3>

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
	{/snippet}
</CompaniesLayout>

{#await data.companyDetails}
	<div><span>Loading...</span></div>
{:then myData}
	{#await data.companyCategoryApps}
		<div><span>Loading...</span></div>
	{:then tableData}
		{#if typeof tableData == 'string'}
			Failed to load company's apps.
		{:else}
			<CompanyTableGrid>
				<!-- @migration-task: migrate this slot by hand, `sdk-android-total-apps` is an invalid identifier -->
	<span slot="sdk-android-total-apps">
					{formatNumber(myData.categories[company_category].sdk_android_total_apps)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `sdk-ios-total-apps` is an invalid identifier -->
	<span slot="sdk-ios-total-apps">
					{formatNumber(myData.categories[company_category].sdk_ios_total_apps)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `adstxt-android-total-apps` is an invalid identifier -->
	<span slot="adstxt-android-total-apps">
					{formatNumber(myData.categories[company_category].adstxt_direct_android_total_apps)}
				</span>
				<!-- @migration-task: migrate this slot by hand, `adstxt-ios-total-apps` is an invalid identifier -->
	<span slot="adstxt-ios-total-apps">
					{formatNumber(myData.categories[company_category].adstxt_direct_ios_total_apps)}
				</span>

				<!-- @migration-task: migrate this slot by hand, `sdk-android` is an invalid identifier -->
	<div slot="sdk-android">
					{#if typeof tableData == 'string'}
						Failed to load company's apps.
					{:else if tableData.sdk.android.apps}
						<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
					{:else}
						Failed to load company overview.
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `sdk-ios` is an invalid identifier -->
	<div slot="sdk-ios">
					{#if tableData.sdk.ios.apps}
						<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `adstxt-android` is an invalid identifier -->
	<div slot="adstxt-android">
					{#if tableData.adstxt_direct.android.apps}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.android.apps} />
					{/if}
				</div>
				<!-- @migration-task: migrate this slot by hand, `adstxt-ios` is an invalid identifier -->
	<div slot="adstxt-ios">
					{#if tableData.adstxt_direct.ios.apps}
						<CompanyOverviewTable entries_table={tableData.adstxt_direct.ios.apps} />
					{/if}
				</div>
			</CompanyTableGrid>
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
{/await}
