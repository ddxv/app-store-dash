<script lang="ts">
	import { page } from '$app/stores';
	import { homeCollectionSelection } from '../stores';
	import { homeStoreSelection } from '../stores';
	import { homeCategorySelection } from '../stores';

	import SideBarRankings from './SideBarRankings.svelte';
	import SideBarCollections from './SideBarCollections.svelte';
	import SideBarCompanies from './SideBarCompanies.svelte';

	let localHomeCollectionSelect = $homeCollectionSelection;
	let localHomeStoreSelect = $state($homeStoreSelection);
	let localHomeCategorySelect = $state($homeCategorySelection);
	import type { CatData } from '../types';

	interface Props {
		myCatData: CatData;
	}

	let { myCatData }: Props = $props();

	// Reactive statement to update the store when localValue changes
	$effect(() => {
		homeCollectionSelection.set(localHomeCollectionSelect);
	});
	$effect(() => {
		homeStoreSelection.set(localHomeStoreSelect);
	});
	$effect(() => {
		if ($page.params.category) {
			localHomeCategorySelect = $page.params.category;
		}
	});
	$effect(() => {
		homeCategorySelection.set(localHomeCategorySelect);
	});
	// For adtech
	let store = $state(1);
	$effect(() => {
		store = +$page.params.store;
	});
	let collection = $state(1);
	$effect(() => {
		collection = +$page.params.collection;
	});
	let category = $state(1);
	$effect(() => {
		category = +$page.params.category;
	});
	// Logic to adjust collection and category based on the store's value
	$effect(() => {
		// If store is not a number (NaN), default it to 1
		if (isNaN(store)) {
			store = 1;
		}

		switch (store) {
			case 2:
				collection = 4;
				category = 120;
				break;
			case 1:
			default: // Defaults for store=1 or any other value not explicitly handled
				collection = 1;
				category = 1;
				break;
		}
	});
</script>

{#if $page.url.pathname.startsWith('/collections')}
	<SideBarCollections {myCatData} />
{/if}

{#if $page.url.pathname == '/rankings' || $page.url.pathname.startsWith('/rankings')}
	<SideBarRankings />
{/if}

{#if $page.url.pathname == '/companies' || $page.url.pathname.startsWith('/companies')}
	<SideBarCompanies {myCatData} />
{/if}


