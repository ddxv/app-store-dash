<script lang="ts">
	import type { TopCompaniesInfo } from '../../../../types';
	import AdtechNav from '$lib/AdtechNav.svelte';
	import { page } from '$app/stores';
	import AdtechTable from '$lib/AdtechTable.svelte';
	export let data: TopCompaniesInfo;

	let entityGroup = 'networks';
	let granularityGroup = 'brands';
	let timeGroup = 'month';

	// React to changes in the current path
	$: {
		if ($page.url.pathname.startsWith('/adtech/networks')) {
			entityGroup = 'networks';
		} else if ($page.url.pathname.startsWith('/adtech/trackers')) {
			entityGroup = 'trackers';
		}
	}

	// React to changes in query parameters
	$: {
		granularityGroup = $page.url.searchParams.get('groupby') || 'parents';
	}
	$: {
		timeGroup = $page.url.searchParams.get('time') || 'month';
	}

	import { homeCategorySelection } from '../../../../stores';
</script>

<svelte:head>
	<title>Ad {entityGroup} stats</title>
	<meta
		name="description"
		content="Explore top advertising networks and third party trackers data across the mobile ad ecosystem for ios and android."
	/>
</svelte:head>

<div class="card p-2 px-4 md:px-16">
	<h3 class="h4 md:h3 p-4">Third Party Mobile Ad Tech Partners</h3>

	<p class="p-4">
		These ad networks and tracker integrations are crawled for the top ~11k Android apps based on
		thos apps that have been in the top 200 ranks for each category since February 2024. The data is
		based on a decompiled Android APK and picking known values from the app's Android Manifests. If
		you have any trackers or networks you'd like to see added feel free to reach out and they can be
		added.
	</p>

	<AdtechNav></AdtechNav>

	{#if entityGroup === 'networks'}
		<p class="p-4">
			Ad Networks will require an SDK to be used to manage the serving of their ads. AppGoblin is
			scanning apps to get an idea of which apps use which networks.
		</p>

		{#await data.networks}
			Loading Ad Networks...
		{:then networks}
			{#if timeGroup === 'month'}
				{#if granularityGroup === 'parents'}
					<AdtechTable
						tabledata={networks.monthly_parent_companies[$homeCategorySelection]}
						tableType="installs"
					></AdtechTable>
				{:else}
					<AdtechTable
						tabledata={networks.monthly_all_companies[$homeCategorySelection]}
						tableType="installs"
					></AdtechTable>
				{/if}
			{:else if granularityGroup === 'parents'}
				<AdtechTable tabledata={networks.parent_companies[$homeCategorySelection]}></AdtechTable>
			{:else}
				<AdtechTable tabledata={networks.all_companies[$homeCategorySelection]}></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
	{#if entityGroup === 'trackers'}
		{#await data.trackers}
			Loading Ad Trackers...
		{:then trackers}
			<p class="p-4">
				Tracking users in apps for marketing purposes is much harder in apps than on the regular
				web. Therefor most apps use other services embedded in their APKs to track users.
			</p>

			{#if timeGroup === 'month'}
				{#if granularityGroup === 'parents'}
					<AdtechTable
						tabledata={trackers.monthly_parent_companies[$homeCategorySelection]}
						tableType="installs"
					></AdtechTable>
				{:else}
					<AdtechTable
						tabledata={trackers.monthly_all_companies[$homeCategorySelection]}
						tableType="installs"
					></AdtechTable>
				{/if}
			{:else if granularityGroup === 'parents'}
				<AdtechTable tabledata={trackers.parent_companies[$homeCategorySelection]}></AdtechTable>
			{:else}
				<AdtechTable tabledata={trackers.all_companies[$homeCategorySelection]}></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
</div>

<a href="/"><p>Back to Home</p></a>
