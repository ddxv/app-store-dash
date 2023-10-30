<script lang="ts">
	import type { CategoryResponse } from '../../../types';
	/** @type {import('../[category]/$types').PageData} */
	export let data: CategoryResponse;
	import AppsCard from '$lib/AppGroupCard.svelte';
</script>

<div>
	{#await data}
		<div>
			<span>Loading...</span>
		</div>
	{:then data}
		{#if data.results}
			<h1 class="h1 p-2">Apps: {data.results.key} {data.results.ios.title}</h1>
			<AppsCard apps={data.results['ios']} />
			<h1 class="h1 p-2">Apps: {data.results.key} {data.results.google.title}</h1>
			<AppsCard apps={data.results['google']} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
