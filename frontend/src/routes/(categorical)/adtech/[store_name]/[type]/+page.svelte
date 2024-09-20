<script lang="ts">
	import type { TopCompaniesInfo } from '../../../../../types';
	import AdtechNav from '$lib/AdtechNav.svelte';
	import { page } from '$app/stores';
	import AdtechTable from '$lib/AdtechTable.svelte';
	import { homeCategorySelection } from '../../../../../stores';
	export let data: TopCompaniesInfo;

	$: console.log('homeCategorySelection:', $homeCategorySelection);

	// TODO: This categorySelection is shared with the numerical one used on other pages!
	function isNumeric(value: string | number): boolean {
		// If the value is a number, check if it's finite.
		if (typeof value === 'number') {
			return isFinite(value);
		}

		// If the value is a string, try parsing it as a float.
		return !isNaN(parseFloat(value)) && isFinite(parseFloat(value));
	}
	// Set categorySelection based on whether the value is numeric or null
	$: categorySelection =
		isNumeric($homeCategorySelection) || $homeCategorySelection === null
			? 'overall'
			: $homeCategorySelection;

	$: store_name = $page.params.store_name || 'Google';
	$: store_id = $page.params.store_name === 'Google' || !$page.params.store_name ? 1 : 2;

	$: entityGroup = $page.params.type || 'networks';

	// React to changes in query parameters
	$: granularityGroup = $page.url.searchParams.get('groupby') || 'parents';
	$: metricName = $page.url.searchParams.get('metric') || 'installs';
</script>

<svelte:head>
	<!-- Title -->
	<title>{entityGroup} AdTech Networks Analysis | App Count by Brand | AppGoblin</title>

	<!-- Standard meta tags -->
	<meta
		name="description"
		content="Explore comprehensive data on AdTech networks used in {entityGroup} apps. Compare popular ad networks, data collectors, and tools by app count and brand. Gain insights into mobile app advertising trends."
	/>
	<meta
		name="keywords"
		content="AdTech networks, Google Play apps, mobile advertising, app analytics, data collectors, SDK analysis, brand comparison, app count metrics, advertising trackers"
	/>

	<!-- Open Graph meta tags -->
	<meta
		property="og:title"
		content="Google Play AdTech Networks: App Count Analysis by Brand | AppGoblin"
	/>
	<meta
		property="og:description"
		content="Dive into detailed analytics of AdTech networks in Google Play apps. Compare top ad networks, data collectors, and tools used across brands. Uncover mobile advertising trends with AppGoblin's comprehensive data."
	/>
	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta
		property="og:url"
		content="https://appgoblin.info/adtech/Google/networks?groupby=brands&metric=appcount"
	/>
	<meta property="og:type" content="website" />

	<!-- Twitter Card meta tags -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta
		name="twitter:title"
		content="Google Play AdTech Networks: Brand & App Count Analysis | AppGoblin"
	/>
	<meta
		name="twitter:description"
		content="Explore which AdTech networks are most popular in Google Play apps. Compare brands, analyze app counts, and uncover mobile advertising trends with AppGoblin's in-depth data."
	/>
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />

	<!-- Additional meta tags -->
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta name="robots" content="index, follow" />
	<link
		rel="canonical"
		href="https://appgoblin.info/adtech/Google/networks?groupby=brands&metric=appcount"
	/>
</svelte:head>

<div class="card p-2 px-4 md:px-16">
	<h2 class="h4 md:h3 p-4">Third Party Mobile Ad Tech Partners</h2>

	<p class="p-4">
		These ad networks and tracker integrations are crawled for the top Android and iOS apps based on
		thos apps that have been in the top 200 ranks for each category since February 2024. The data is
		based on a decompiled Android APK and unzipped iOS IPAs. Then picking known values from the
		app's Android Manifests and iOS plist files. Roughly 15k apps for Android and 1k for iOS have
		been scanned.
	</p>
	<p>
		If you have any trackers or networks you'd like to see added feel free to reach out and they can
		be added.
	</p>
	{#if entityGroup === 'networks'}
		<p class="p-4">
			Ad Networks will require an SDK to be used to manage the serving of their ads. AppGoblin is
			scanning apps to get an idea of which apps use which networks.
		</p>
	{/if}
	{#if entityGroup === 'trackers'}
		<p class="p-4">
			Tracking users in apps for marketing purposes is much harder in apps than on the regular web.
			Therefor most apps use other services embedded in their APKs to track users.
		</p>
	{/if}

	<AdtechNav></AdtechNav>

	{#await data.mycats}
		waiting for data...
	{:then cats}
		{#each Object.entries(cats.categories) as [_prop, values]}
			{#if values.id == categorySelection}
				{#if entityGroup == 'networks'}
					<h1 class="h3 md:h2 p-4">Ad Networks, Category: {values.name}</h1>
				{/if}
				{#if entityGroup == 'trackers'}
					<h1 class="h3 md:h2 p-4">MMPs, Category: {values.name}</h1>
				{/if}
			{/if}
		{/each}
	{/await}

	{#if entityGroup === 'networks'}
		{#await data.networks}
			Loading Ad Networks...
		{:then networks}
			{#if granularityGroup === 'parents'}
				<AdtechTable
					tabledata={networks.parent_companies[store_id][categorySelection]}
					tableType={metricName}
					storeId={store_id}
					{store_name}
				></AdtechTable>
			{:else}
				<AdtechTable
					tabledata={networks.all_companies[store_id][categorySelection]}
					tableType={metricName}
					storeId={store_id}
					{store_name}
				></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
	{#if entityGroup === 'trackers'}
		{#await data.trackers}
			Loading Ad Trackers...
		{:then trackers}
			{#if granularityGroup === 'parents'}
				<AdtechTable
					tabledata={trackers.parent_companies[store_id][categorySelection]}
					tableType={metricName}
					storeId={store_id}
					{store_name}
				></AdtechTable>
			{:else}
				<AdtechTable
					tabledata={trackers.all_companies[store_id][categorySelection]}
					tableType={metricName}
					storeId={store_id}
					{store_name}
				></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
</div>

<a href="/"><p>Back to Home</p></a>
