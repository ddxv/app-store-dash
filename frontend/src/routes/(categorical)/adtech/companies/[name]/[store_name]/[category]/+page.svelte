<script lang="ts">
	import type { CompanyApps } from '../../../../../../../types';
	export let data: CompanyApps;
	import AppsCard from '$lib/AppGroupCard.svelte';

	import { page } from '$app/stores';

	var osName: string;

	$: store_name = $page.params.store_name;

	$: if (store_name == 'Google') {
		osName = 'Google Android';
	} else {
		osName = 'Apple iOS';
	}

	$: company_category = $page.params.category;
	$: company_name = $page.params.name;
</script>

<div>
	{#await data.results}
		<div>
			<span>Loading...</span>
		</div>
	{:then apps}
		{#if typeof apps == 'string'}
			Failed to load network's apps.
		{:else}
			{#if apps.title == 'No Trackers Found'}
				<h1 class="h1 p-2">Top Apps with No Trackers Found</h1>
				<p class="h4 p-4">
					These are apps that we don't yet have mappings for. If you are able to recognize a tracker
					in any of the data available on their respective pages feel free to reach out and they
					will be categorized accordingly.
				</p>
			{:else}
				<h1 class="h1 p-2">{apps.title}'s top {company_category} apps for {osName}</h1>
				<p class="h4 p-4">
					These are the apps we currently have which have at least one reference to the network in
					their decompiled app.
				</p>
			{/if}
			<AppsCard {apps} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
