<script lang="ts">
	import { page } from '$app/stores';

	import SideBarCatsListBoxItem from './SideBarCatsListBoxItem.svelte';

	import { homeCollectionSelection } from '../stores';
	let localHomeCollectionSelect = $state($homeCollectionSelection);
	// Reactive statement to update the store when localValue changes
	$effect(() => {
		homeCollectionSelection.set(localHomeCollectionSelect);
	});

	import { homeStoreSelection } from '../stores';
	let localHomeStoreSelect = $state($homeStoreSelection);
	$effect(() => {
		homeStoreSelection.set(localHomeStoreSelect);
	});

	import { homeCategorySelection } from '../stores';
	let localHomeCategorySelect = $state($homeCategorySelection);
	$effect(() => {
		homeCategorySelection.set(localHomeCategorySelect);
	});

	import type { CatData } from '../types';

	$effect(() => {
		if ($page.params.category) {
			localHomeCategorySelect = $page.params.category;
		} else {
			localHomeCategorySelect = 'overall';
		}
	});

	interface Props {
		baseUrl: string;
		myCatData: CatData;
	}

	let { baseUrl, myCatData }: Props = $props();
	import CardFirst from './CardFirst.svelte';
</script>

<div class="p-1 md:p-2">
	<CardFirst>
		{#snippet header()}
			<h3 class="h5 md:h4">App Categories</h3>
		{/snippet}
		{#if myCatData}
			{#each Object.entries(myCatData.categories) as [_prop, values]}
				{#if values.id && (Number(values.android) > 0 || values.name == 'Games')}
					{#if values.id != 'overall'}
						<a href="{baseUrl}/{values.id}" class="text-tertiary-900-100 hover:underline">
							<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
						</a>
					{:else if baseUrl == '/companies/categories' && values.id == 'overall'}
						<a href="/companies" class="text-tertiary-900-100 hover:underline">
							<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
						</a>
					{:else}
						<a href={baseUrl} class="text-tertiary-900-100 hover:underline">
							<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
						</a>
					{/if}
				{/if}
			{/each}
		{/if}
	</CardFirst>
</div>
