<script lang="ts">
	import type { Collections } from '../../../types';
	/** @type {import('../[collection]/$types').PageData} */
	export let data: Collections;
	import AppsCard from '$lib/AppGroupCard.svelte';

	import { myStoreSelection } from '../../../stores';
	import { myCategorySelection } from '../../../stores';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<div>
	{#if data.myapps}
		<h1 class="h1 p-2">Apps: {data.myapps.title}</h1>
		{#each Object.entries(data.myapps.categories) as [_key, cat]}
			{#if cat.key == $myCategorySelection}
				<!-- {#each cat[$myStoreSelection].apps as app} -->
				<AppsCard apps={cat[$myStoreSelection]} />
				<p class="p-2" />
			{/if}
		{/each}
	{:else}
		<p>Loading...</p>
		{data}
	{/if}
</div>
