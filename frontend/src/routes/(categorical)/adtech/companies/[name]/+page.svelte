<script lang="ts">
	import type { CompanyFullDetails } from '../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	export let data: CompanyFullDetails;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';
	import CompanyCategoryPie from '$lib/CompanyCategoryPie.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';
	import CompanyTree from '$lib/CompanyTree.svelte';
	import CompanySDKs from '$lib/CompanySDKs.svelte';

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<div class="bg-white p-6 rounded-lg shadow-md">
		<h1 class="text-3xl font-bold mb-6 text-gray-800">{name}</h1>
		{#await data.companyTree}
			<div class="bg-white p-6 rounded-md shadow-md flex justify-center items-center h-40">
				<span class="text-lg text-gray-600">Loading...</span>
			</div>
		{:then myTree}
			{#if typeof myTree == 'string'}
				<p class="text-red-500 text-center">Failed to load company tree.</p>
			{:else if myTree}
				<p class="text-gray-700">Domain: {myTree.parent_company_domain}</p>
			{/if}
		{:catch error}
			<p class="text-red-500 text-center">{error.message}</p>
		{/await}

		<CompanyCategoryPie />

		<div class="lg:col-span-1">
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
							<span class="font-semibold text-gray-900">{formatNumber(myData.total_apps)}</span>
						</p>
					</div>
				{/if}
			{:catch error}
				<p class="text-red-500 text-center">{error.message}</p>
			{/await}
		</div>
	</div>

	{#await data.companyTree}
		<div class="bg-white p-6 rounded-md shadow-md flex justify-center items-center h-40">
			<span class="text-lg text-gray-600">Loading...</span>
		</div>
	{:then myTree}
		{#if typeof myTree == 'string'}
			<p class="text-red-500 text-center">Failed to load company tree.</p>
		{:else if myTree && myTree.children_companies.length > 0}
			<CompanyTree {myTree} />
		{/if}
	{:catch error}
		<p class="text-red-500 text-center">{error.message}</p>
	{/await}

	<div class="lg:col-span-3">
		{#await data.companySdks}
			<div class="bg-white p-6 rounded-lg shadow-md flex justify-center items-center h-40">
				<span class="text-lg text-gray-600">Loading...</span>
			</div>
		{:then mySdks}
			{#if typeof mySdks == 'string'}
				<p class="text-red-500 text-center">Failed to load company SDKs.</p>
			{:else if mySdks}
				<div class="bg-white p-6 rounded-lg shadow-md">
					<CompanySDKs {mySdks} />
				</div>
			{/if}
		{/await}
	</div>
</div>
{#await data.companyDetails}
	<div><span>Loading...</span></div>
{:then myData}
	<CompanyTableGrid>
		<span slot="sdk-android-total-apps">
			{formatNumber(myData.sdk_android_total_apps)}
		</span>
		<span slot="sdk-ios-total-apps">
			{formatNumber(myData.sdk_ios_total_apps)}
		</span>
		<span slot="adstxt-android-total-apps">
			{formatNumber(myData.adstxt_android_total_apps)}
		</span>
		<span slot="adstxt-ios-total-apps">
			{formatNumber(myData.adstxt_ios_total_apps)}
		</span>

		<div slot="sdk-android">
			{#await data.companyOverview}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData}
					<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
				{:else}
					Failed to load company overview.
				{/if}
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}
		</div>
		<div slot="sdk-ios">
			{#await data.companyOverview}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData}
					<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
				{/if}
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}
		</div>
		<div slot="adstxt-android">
			{#await data.companyOverview}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData}
					<CompanyOverviewTable entries_table={tableData.adstxt.android.apps} />
				{/if}
			{/await}
		</div>
		<div slot="adstxt-ios">
			{#await data.companyOverview}
				<div><span>Loading...</span></div>
			{:then tableData}
				{#if typeof tableData == 'string'}
					Failed to load company's apps.
				{:else if tableData}
					<CompanyOverviewTable entries_table={tableData.adstxt.ios.apps} />
				{/if}
			{/await}
		</div>
	</CompanyTableGrid>
{/await}
