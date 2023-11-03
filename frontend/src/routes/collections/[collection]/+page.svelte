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
	{#await data.AppCollections.streamed}
		<title>App Stats & Info</title>
	{:then myapps}
		{#if typeof myapps != 'string'}
			<title>{myapps.title} App Stats & Info</title>
		{:else}
			<title>App Stats & Info</title>
		{/if}
	{/await}
	<meta
		name="description"
		content="Explore comprehensive app analytics and market trends across Google Play and iTunes with AppGoblin. Dive into detailed app rankings and download statistics to inform your app strategy and discover top-performing apps."
	/>
	<meta
		name="keywords"
		content="app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
	/>
</svelte:head>

{#await data.AppCollections.streamed}
	<div>
		<span>Loading data...</span>
	</div>
{:then myapps}
	{#if typeof myapps != 'string'}
		<h1 class="h1 p-2">Apps: {myapps.title}</h1>
		{#each Object.entries(myapps.categories) as [_key, cat]}
			{#if cat.key == $homeCategorySelection}
				<AppsCard apps={cat[$homeStoreSelection]} />
				<p class="p-2" />
			{/if}
		{/each}
	{:else}
		<p>Loading data failed due to internal error.</p>
	{/if}
{:catch error}
	<!-- NOTE: This is currently not displaying -->
	<p style="color: red">{error.message}</p>
{/await}
