<script lang="ts">
	import type { SearchResponse } from '../../../types';

	import AppGroupCard from '$lib/AppGroupCard.svelte';

	export let data: SearchResponse;
</script>

{#await data.results.streamed}
	Loading ...
{:then results}
	<AppGroupCard apps={results} />
{:catch}
	Loading ...
{/await}
