<script lang="ts">
	import type { TopCompaniesInfo } from '../../../types';
	import AdtechNav from '$lib/AdtechNav.svelte';
	import { page } from '$app/stores';
	import AdtechTable from '$lib/AdtechTable.svelte';
	export let data: TopCompaniesInfo;

	function navigate(name: string) {
		window.location.href = `/adtech/companies/${name}`;
	}
	let entityGroup = 'networks';
	let granularityGroup = 'brands';

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
</script>

<svelte:head>
	<title>Ad {entityGroup} stats</title>
	<meta
		name="description"
		content="Explore top advertising networks and third party trackers data across the mobile ad ecosystem for ios and android."
	/>
</svelte:head>

<div class="card p-2 md:p-16">
	<h3 class="h4 md:h3 p-4">Third Party Mobile Ad Tech Partners</h3>

	<AdtechNav></AdtechNav>

	{#if entityGroup === 'networks'}
		<p class="p-4">
			For an app to make money from advertising, the owner of the app will usually use an Ad Network
			to sell their apps's advertising space. These Ad Networks will require an SDK to be used to
			manage the ad itself. AppGoblin is scanning apps to get an idea of which apps use which
			networks. Currently this list is for Android APKs only.
		</p>

		{#await data.networks.streamed}
			Loading Ad Networks...
		{:then networks}
			{#if granularityGroup === 'parents'}
				<AdtechTable tabledata={networks.parent_companies}></AdtechTable>
			{:else}
				<AdtechTable tabledata={networks.companies}></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
	{#if entityGroup === 'trackers'}
		{#await data.trackers.streamed}
			Loading Ad Trackers...
		{:then trackers}
			<p class="p-4">
				Tracking users in apps for marketing purposes is much harder in apps than on the regular
				web. Therefor most apps use other services embedded in their APKs to track users. AppGoblin
				is scanning apps to get an idea of which apps use which trackers. Currently this list is for
				Android APKs only.
			</p>
			{#if granularityGroup === 'parents'}
				<AdtechTable tabledata={trackers.parent_companies}></AdtechTable>
			{:else}
				<AdtechTable tabledata={trackers.companies}></AdtechTable>
			{/if}
		{:catch}
			Problem loading data
		{/await}
	{/if}
</div>

<a href="/"><p>Back to Home</p></a>
