<script lang="ts">
	import type { DeveloperResponse } from '../../../types';
	import AppsCard from '$lib/AppGroupCard.svelte';
	interface Props {
		data: DeveloperResponse;
	}

	let { data }: Props = $props();
</script>

<div>
	{#await data.results}
		<div>
			<span>Loading...</span>
		</div>
	{:then devs}
		{#if typeof devs == 'string'}
			Failed to load developer
		{:else}
			<h1 class="h1 p-2">Apps: {devs.title}</h1>
			<AppsCard apps={devs} />
			<p class="p-2"></p>
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
