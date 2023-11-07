<script lang="ts">
	import type { DeveloperResponse } from '../../../types';
	export let data: DeveloperResponse;
	import AppsCard from '$lib/AppGroupCard.svelte';
</script>

<div>
	{#await data.results.streamed}
		<div>
			<span>Loading...</span>
		</div>
	{:then devs}
		{#if typeof devs == 'string'}
			Failed to load developer
		{:else}
			<h1 class="h1 p-2">Apps: {devs.title}</h1>
			<AppsCard apps={devs} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
