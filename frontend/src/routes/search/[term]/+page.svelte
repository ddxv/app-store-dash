<script lang="ts">
	import type { SearchResponse } from '../../../types';

	import AppGroupCard from '$lib/AppGroupCard.svelte';

	/** @type {import('../[term]/$types').PageData} */
	export let data: SearchResponse;
</script>

{#if data.results}
	<AppGroupCard apps={data.results} />
{/if}
