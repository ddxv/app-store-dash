<script lang="ts">
	import type { Collections } from '../../../types';
	/** @type {import('../[collection]/$types').PageData} */
	export let data: Collections;
	import AppsCard from '$lib/AppGroupCard.svelte';

	import { homeStoreSelection } from '../../../stores';
	import { homeCategorySelection } from '../../../stores';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<svelte:head>
	{#if data.myapps}
		<title>{data.myapps.title} App Stats & Info</title>
		<meta
			name="description"
			content="Explore comprehensive app analytics and market trends across Google Play and iTunes with AppGoblin. Dive into detailed app rankings and download statistics to inform your app strategy and discover top-performing apps."
		/>
		<meta
			name="keywords"
			content="app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
		/>
	{/if}
</svelte:head>

<div>
	{#await data}
		<div>
			<span>Loading...</span>
		</div>
	{:then data}
		{#if data.myapps}
			<h1 class="h1 p-2">Apps: {data.myapps.title}</h1>
			{#each Object.entries(data.myapps.categories) as [_key, cat]}
				{#if cat.key == $homeCategorySelection}
					<AppsCard apps={cat[$homeStoreSelection]} />
					<p class="p-2" />
				{/if}
			{/each}
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
