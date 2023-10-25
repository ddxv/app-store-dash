<script lang="ts">
	import type { CategoryResponse } from '../../../types';
	/** @type {import('../[category]/$types').PageData} */
	export let data: CategoryResponse;
	import AppsCard from '$lib/AppGroupCard.svelte';

	import { myStoreSelection } from '../../../stores';
	import { myCategorySelection } from '../../../stores';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<div>
	{#await data}
		<div>
			<span>Loading...</span>
		</div>
	{:then data}
		{#if data.results}
			<h1 class="h1 p-2">Apps: {data.results.key}</h1>
			<h1 class="h1 p-2">Apps: {data.results.key} {data.results['google'].apps}</h1>
			<h1 class="h1 p-2">Apps: {data.results.key} {Object.keys(data.results['ios'].apps)}</h1>
			<AppsCard apps={data.results['ios']} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
