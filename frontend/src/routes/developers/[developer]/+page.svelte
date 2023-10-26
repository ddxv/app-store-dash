<script lang="ts">
	import type { DeveloperResponse } from '../../../types';
	/** @type {import('../[developer]/$types').PageData} */
	export let data: DeveloperResponse;
	import AppsCard from '$lib/AppGroupCard.svelte';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<div>
	{#await data}
		<div>
			<span>Loading...</span>
		</div>
	{:then data}
		{#if data.results}
			<h1 class="h1 p-2">Apps: {data.results.title}</h1>
			<AppsCard apps={data.results} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
