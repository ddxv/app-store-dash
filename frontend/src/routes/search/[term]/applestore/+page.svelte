<script lang="ts">
	import type { AppleStoreSearchResponse } from '../../../../types';

	import AppGroupCard from '$lib/AppGroupCard.svelte';

	export let data: AppleStoreSearchResponse;
</script>

{#await data.results}
	Loading ...
{:then results}
	{#if typeof results != 'string'}
		{#if results.apps.length > 0}
			<!-- <pre>{JSON.stringify(results, null, 2)}</pre> -->
			<AppGroupCard apps={results} />
		{:else}
			<h3 class="h3">No apps found, please try your search again.</h3>
		{/if}
	{:else}
		<p>Search failed please try again ... {results}</p>
	{/if}
{:catch error}
	<p>Search failed please try again ... {error.message}</p>
{/await}
