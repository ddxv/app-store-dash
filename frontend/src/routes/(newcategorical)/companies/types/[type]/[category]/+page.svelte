<script lang="ts">
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
	import CompaniesTableGrid from '$lib/CompaniesTableGrid.svelte';

	import { page } from '$app/stores';

	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let appCategory = $derived($page.params.category);
	let companyType = $derived($page.params.type);

	let { data }: Props = $props();

	let currentType = $derived(
		data.companyTypes.then((myTypes) =>
			myTypes.types.find((type: { url_slug: string }) => type.url_slug === companyType)
		)
	);

	let currentCategory = $derived(
		data.appCats.then((catsData) =>
			catsData.categories.find((cat: { id: string }) => cat.id == appCategory)
		)
	);

	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

{#await currentType}
	<div><span>Loading...</span></div>
{:then type}
	<div class="flex items-center mb-2">
		<h1 class="text-3xl font-bold text-primary-900-100">
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
			{#snippet mainTable()}
				{#if tableData && tableData.companies_overview.length > 0}
					<CompaniesOverviewTable entries_table={tableData.companies_overview} />
				{/if}
			{/snippet}
			{#snippet sdkAndroidTotalApps()}
				Android Companies: {formatNumber(
					tableData.categories.categories.companies.sdk_android_total_companies
				)}
			{/snippet}
			{#snippet sdkIosTotalApps()}
				iOS Companies: {formatNumber(
					tableData.categories.categories.companies.sdk_ios_total_companies
				)}
			{/snippet}
			{#snippet adstxtAndroidTotalApps()}
				Android Companies: {formatNumber(
					tableData.categories.categories.companies.adstxt_direct_android_total_companies
				)}
			{/snippet}
			{#snippet adstxtIosTotalApps()}
				iOS Companies: {formatNumber(
					tableData.categories.categories.companies.adstxt_direct_ios_total_companies
				)}
			{/snippet}
		</CompaniesTableGrid>
	{/if}
{/await}
