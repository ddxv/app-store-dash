<script lang="ts">
	import { page } from '$app/stores';
	import type { SearchResponse } from '../../../types';
	import AppGroupCard from '$lib/AppGroupCard.svelte';
	import { goto } from '$app/navigation';

	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';

	interface Props {
		data: SearchResponse;
	}

	let { data }: Props = $props();
	let searchTerm: string | null = $state($page.params.term || '');

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

<h1 class="h1">Search Results for {searchTerm}</h1>

<div class="p-4">
	{#await data.companiesResults}
		Loading ...
	{:then companiesResults}
		{#if typeof companiesResults != 'string'}
			<h2 class="h2 p-4">Companies</h2>
			{#if companiesResults.length > 0}
				<CompaniesOverviewTable entries_table={companiesResults} />
			{:else}
				<h3 class="h3 p-4">
					No adtech/business/ development tool companies found, if you expected to see something
					please let us know by sending a note on Discord or GitHub and we can add it.
				</h3>
			{/if}
		{:else}
			<p>Search failed please try again ...</p>
		{/if}
	{:catch error}
		<p>Search failed please try again ... {error.message}</p>
	{/await}
</div>

<div class="p-4">
	{#await data.results}
		Loading ...
	{:then results}
		{#if typeof results != 'string'}
			{#if results.apps.length > 0}
				<AppGroupCard apps={results} />
			{:else}
				<h2 class="h2 p-4">Apps</h2>
				<h3 class="h3">No apps found, please try your search again.</h3>
			{/if}
			<div class="card p-4 mt-4">
				<h3 class="h3">Didn't see what you're looking for?</h3>
				<p class="p-2">
					Try searching on Google Play. Results will take an hour to be live on AppGoblin. If you
					still don't see what you're looking for please reach out on GitHub or Discord.
				</p>
				<card class="card preset-tonal p-4">
					<button class="btn variant-filled-primary p-2" onclick={searchGooglePlay}>
						Search Google Play Store
					</button>
				</card>
				<card class="card preset-tonal p-4">
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
</div>
