<script lang='ts'>
	import CompaniesOverviewTable from "$lib/CompaniesOverviewTable.svelte";
	import CompaniesTableGrid from "$lib/CompaniesTableGrid.svelte";

    import { page } from '$app/stores';

    import { type CompaniesOverview } from "../../../../../types";

	import type { PageData } from "../$types";

    export let data: PageData;

    function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}

	$: currentType = data.companyTypes.then(myTypes => 
        myTypes.types.find((type: { url_slug: string }) => type.url_slug === $page.params.type)
    );

	

</script>


{#await currentType}
<div><span>Loading...</span></div>
{:then type}
<div class="flex items-center mb-2">
<h1 class="text-3xl font-bold text-gray-800">

	{type ? type.name : 'Unknown'} / {#if $page.params.category} {$page.params.category} {:else}  All App Categories  {/if} 
</h1>
<div class="h-8 w-px bg-gray-300 mx-2"></div>
</div>
{/await}

{#await data.companiesOverview}
	<div><span>Loading...</span></div>
{:then tableData}
	{#if typeof tableData == 'string'}
		Failed to load companies.
	{:else if tableData.categories}
			<CompaniesTableGrid>

			<div slot="main-table">
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			</div>
            			<span slot="sdk-android-total-apps"
				>Android Companies:
				{formatNumber(tableData.categories.categories.all.sdk_android_total_apps)}
			</span>
			<span slot="sdk-ios-total-apps">
				iOS Companies: {formatNumber(tableData.categories.categories.all.sdk_ios_total_apps)}
			</span>
			<span slot="adstxt-android-total-apps">
				Android Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_direct_android_total_apps
				)}
			</span>
			<span slot="adstxt-ios-total-apps">
				iOS Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_direct_ios_total_apps
				)}
			</span>

			
			</CompaniesTableGrid>
	{/if}

{/await}

