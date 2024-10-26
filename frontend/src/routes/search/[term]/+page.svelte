<script lang="ts">
	import { run } from 'svelte/legacy';

	import { page } from '$app/stores';
	import type { SearchResponse } from '../../../types';
	import AppGroupCard from '$lib/AppGroupCard.svelte';
	import { goto } from '$app/navigation';

	interface Props {
		data: SearchResponse;
	}

	let { data }: Props = $props();
	let searchTerm: string | null = $state('');

	run(() => {
		searchTerm = $page.params.term;
	});

	function searchGooglePlay() {
		if (searchTerm) {
			goto(`/search/${encodeURIComponent(searchTerm)}/playstore`);
		} else {
			console.log('search term error');
		}
	}
	function searchAppleStore() {
		if (searchTerm) {
			goto(`/search/${encodeURIComponent(searchTerm)}/applestore`);
		} else {
			console.log('search term error');
		}
	}
</script>

{#await data.results}
	Loading ...
{:then results}
	{#if typeof results != 'string'}
		{#if results.apps.length > 0}
			<AppGroupCard apps={results} />
		{:else}
			<h3 class="h3">No apps found, please try your search again.</h3>
		{/if}
		<div class="card p-4 mt-4">
			<h3 class="h3">Didn't see what you're looking for?</h3>
			<p class="p-2">
				Try searching on Google Play. Results may take a couple minutes to be live on AppGoblin.
			</p>
			<card class="card variant-glass-surface p-4">
				<button class="btn variant-filled-primary p-2" onclick={searchGooglePlay}>
					Search Google Play Store
				</button>
			</card>
			<card class="card variant-glass-surface p-4">
				<button class="btn variant-filled-primary p-2" onclick={searchAppleStore}>
					Search Apple App Store
				</button>
			</card>
		</div>
	{:else}
		<p>Search failed please try again ... {results}</p>
	{/if}
{:catch error}
	<p>Search failed please try again ... {error.message}</p>
{/await}
