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
