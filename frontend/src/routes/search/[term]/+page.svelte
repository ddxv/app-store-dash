<script lang="ts">
	import type { SearchResponse } from '../../../types';

	import AppGroupCard from '$lib/AppGroupCard.svelte';

	export let data: SearchResponse;
</script>

{#await data.results.streamed}
	Loading ...
{:then results}
	{#if typeof results != 'string'}
		{#if results.apps.length > 0}
			<AppGroupCard apps={results} />
		{:else}
			<h3 class="h3">No apps found, please try your search again.</h3>
		{/if}
	{:else}
		<p>Search failed please try again ... {results}</p>
	{/if}
{:catch error}
	<!-- NOTE: This is currently not displaying -->
	<p>Search failed please try again ... {error.message}</p>
{/await}
