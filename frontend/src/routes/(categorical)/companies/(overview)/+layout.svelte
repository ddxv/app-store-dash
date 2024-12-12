<script lang="ts">
	import CompaniesLayout from '$lib/CompaniesLayout.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';
	import CompaniesBarChart from '$lib/CompaniesBarChart.svelte';
	import TotalsBox from '$lib/TotalsBox.svelte';
	import { page } from '$app/stores';

	import type { Snippet } from 'svelte';

	let { children }: { children: Snippet } = $props();

	let currentType = $derived(
		$page.data.companyTypes.types.find(
			(type: { url_slug: string }) => type.url_slug === $page.params.type
		)
	);

	let currentCategoryName = $derived(getCategoryName($page.params.category));

	function getCategoryName(category: string) {
		return (
			$page.data?.appCats?.categories?.find((cat: { id: string }) => cat.id == category)?.name ||
			category
		);
	}
</script>

<div class="flex items-center mb-2">
	<h1 class="h1 text-3xl font-bold text-primary-900-100">
		Top {#await currentType then currentType}
			<span class="text-primary-700-300">{currentType ? currentType.name : ''}</span>
		{/await}
		companies for
		{#await currentCategoryName then currentCategoryName}
			<span class="text-primary-700-300">{currentCategoryName ? currentCategoryName : 'All'}</span>
		{/await}
		Apps
	</h1>
</div>

<CompaniesLayout>
	{#snippet card1()}
		<WhiteCard>
			{#snippet title()}
				Totals
			{/snippet}
			{#await $page.data.companiesOverview then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else}
					<TotalsBox myTotals={myData.categories.categories.all} myType={currentType} />
				{/if}
			{/await}
		</WhiteCard>
	{/snippet}
	{#snippet card2()}
		<WhiteCard>
			{#snippet title()}
				Top SDK Companies
			{/snippet}
			{#await $page.data.companiesOverview then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else}
					<CompaniesBarChart plotData={myData.top.sdk} />
				{/if}
			{/await}
		</WhiteCard>
	{/snippet}
	{#snippet card3()}
		<WhiteCard>
			{#snippet title()}
				Top Adstxt Companies
			{/snippet}
			{#await $page.data.companiesOverview then myData}
				{#if typeof myData == 'string'}
					<p class="text-red-500 text-center">Failed to load company details.</p>
				{:else}
					<CompaniesBarChart plotData={myData.top.adstxt_direct} />
				{/if}
			{/await}
		</WhiteCard>
	{/snippet}
</CompaniesLayout>

<main>
	<!-- +page.svelte is `@render`ed here -->
	{@render children()}
</main>
