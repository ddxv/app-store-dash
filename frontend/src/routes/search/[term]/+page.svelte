<script lang="ts">
	import type { SearchResponse } from '../../../types';

	import AppGroupCard from '$lib/AppGroupCard.svelte';

	export let data: SearchResponse;
</script>

{#await data.results.streamed}
	Loading ...
{:then results}
	{#if typeof results != 'string'}
		<AppGroupCard apps={results} />
	{:else}
		<p>Search failed please try again ... {results}</p>
	{/if}
{:catch error}
	<!-- NOTE: This is currently not displaying -->
	<p>Search failed please try again ... {error.message}</p>
{/await}
