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
		Top <span class="text-primary-700-300">{currentType ? currentType.name : ''}</span> companies
		for
		<span class="text-primary-700-300">{currentCategoryName ? currentCategoryName : 'All'}</span>
		Apps
	</h1>
</div>

{#await $page.data.companiesOverview then myData}
	{#if typeof myData == 'string'}
		<p class="text-red-500 text-center">Failed to load company details.</p>
	{:else}
		<CompaniesLayout>
			{#snippet card1()}
				<WhiteCard>
					{#snippet title()}
						Totals
					{/snippet}
					<TotalsBox myTotals={myData.categories.categories.all} myType={currentType} />
				</WhiteCard>
			{/snippet}
			{#snippet card2()}
				<WhiteCard>
					{#snippet title()}
						Top SDK Companies
					{/snippet}
					<CompaniesBarChart plotData={myData.top.sdk} />
				</WhiteCard>
			{/snippet}
			{#snippet card3()}
				<WhiteCard>
					{#snippet title()}
						Top Adstxt Companies
					{/snippet}
					<CompaniesBarChart plotData={myData.top.adstxt_direct} />
				</WhiteCard>
			{/snippet}
		</CompaniesLayout>
	{/if}
{:catch error}
	<p class="text-red-500 text-center">{error.message}</p>
{/await}

<main>
	<!-- +page.svelte is `@render`ed here -->
	{@render children()}
</main>
