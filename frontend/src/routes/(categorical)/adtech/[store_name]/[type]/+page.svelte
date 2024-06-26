<script lang="ts">
	import type { TopCompaniesInfo } from '../../../../../types';
	import AdtechNav from '$lib/AdtechNav.svelte';
	import { page } from '$app/stores';
	import AdtechTable from '$lib/AdtechTable.svelte';
	export let data: TopCompaniesInfo;

	let entityGroup = 'networks';
	let granularityGroup = 'brands';
	let metricName = 'installs';

	let store_id = 1;

	$: store_name = $page.params.store_name;
	$: {
		if (store_name == 'Google') {
			store_id = 1;
		} else store_id = 2;
	}

	$: entityGroup = $page.params.type;

	// React to changes in query parameters
	$: {
		granularityGroup = $page.url.searchParams.get('groupby') || 'parents';
	}
	$: {
		metricName = $page.url.searchParams.get('metric') || 'installs';
	}

	import { homeCategorySelection } from '../../../../../stores';
</script>

<svelte:head>
	<title>Ad {entityGroup} stats</title>
	<meta
		name="description"
		content="Explore top advertising networks and third party trackers data across the mobile ad ecosystem for ios and android."
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
			{#if values.id == $homeCategorySelection}
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
					tabledata={networks.parent_companies[store_id][$homeCategorySelection] || {}}
					tableType={metricName}
					storeId={store_id}
					category_name={$homeCategorySelection}
					{store_name}
				></AdtechTable>
			{:else}
				<AdtechTable
					tabledata={networks.all_companies[store_id][$homeCategorySelection] || {}}
					tableType={metricName}
					storeId={store_id}
					category_name={$homeCategorySelection}
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
					tabledata={trackers.parent_companies[store_id][$homeCategorySelection] || {}}
					tableType={metricName}
					storeId={store_id}
					category_name={$homeCategorySelection}
					{store_name}
				></AdtechTable>
			{:else}
				<AdtechTable
					tabledata={trackers.all_companies[store_id][$homeCategorySelection] || {}}
					tableType={metricName}
					storeId={store_id}
					category_name={$homeCategorySelection}
					{store_name}
				></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
</div>

<a href="/"><p>Back to Home</p></a>
