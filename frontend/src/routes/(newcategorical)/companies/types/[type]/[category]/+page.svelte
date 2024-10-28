<script lang="ts">
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
	import CompaniesTableGrid from '$lib/CompaniesTableGrid.svelte';

	import { page } from '$app/stores';

	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let currentType = $derived(data.companyTypes.then((myTypes) =>
		myTypes.types.find((type: { url_slug: string }) => type.url_slug === $page.params.type)
	));

	let currentCategory = $derived(data.appCats.then((catsData) =>
		catsData.categories.find((cat: { id: string }) => cat.id == $page.params.category)
	));

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

{#await currentType}
	<div><span>Loading...</span></div>
{:then type}
	<div class="flex items-center mb-2">
		<h1 class="text-3xl font-bold text-gray-800">
			{type ? type.name : 'Unknown'} -
			{#await currentCategory then myCategory}
				{myCategory ? myCategory.name : 'Unknown'}
			{/await}
		</h1>
	</div>
{/await}

{#await data.companiesOverview}
	<div><span>Loading...</span></div>
{:then tableData}
	{#if typeof tableData == 'string'}
		Failed to load companies.
	{:else if tableData.categories}
		<CompaniesTableGrid>
			<!-- @migration-task: migrate this slot by hand, `main-table` is an invalid identifier -->
	<div slot="main-table">
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			</div>
			<!-- @migration-task: migrate this slot by hand, `sdk-android-total-apps` is an invalid identifier -->
	<span slot="sdk-android-total-apps"
				>Android Companies:
				{formatNumber(tableData.categories.categories.all.sdk_android_total_apps)}
			</span>
			<!-- @migration-task: migrate this slot by hand, `sdk-ios-total-apps` is an invalid identifier -->
	<span slot="sdk-ios-total-apps">
				iOS Companies: {formatNumber(tableData.categories.categories.all.sdk_ios_total_apps)}
			</span>
			<!-- @migration-task: migrate this slot by hand, `adstxt-android-total-apps` is an invalid identifier -->
	<span slot="adstxt-android-total-apps">
				Android Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_direct_android_total_apps
				)}
			</span>
			<!-- @migration-task: migrate this slot by hand, `adstxt-ios-total-apps` is an invalid identifier -->
	<span slot="adstxt-ios-total-apps">
				iOS Companies: {formatNumber(
					tableData.categories.categories.all.adstxt_direct_ios_total_apps
				)}
			</span>
		</CompaniesTableGrid>
	{/if}
{/await}
