<script lang="ts">
	import type { CompanyFullDetails } from '../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	export let data: CompanyFullDetails;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';

	import CompanyTableGrid from '$lib/CompanyTableGrid.svelte';

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<div class="card-content p-6 bg-white shadow-md rounded-lg">
	<h1 class="text-3xl font-bold mb-6 text-gray-800">{name}</h1>
	{#await data.companyDetails}
		<div class="flex justify-center items-center h-40">
			<span class="text-lg text-gray-600">Loading...</span>
		</div>
	{:then myData}
		{#if typeof myData == 'string'}
			<p class="text-red-500 text-center">Failed to load company details.</p>
		{:else if myData}
			<div class="mt-6 bg-white p-6 rounded-lg shadow-md">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
				<p class="text-lg text-gray-700">
					Total: <span class="font-semibold text-gray-900">{formatNumber(myData.total_apps)}</span>
				</p>
			</div>

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
						{:else}
							Failed to load company overview.
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
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
