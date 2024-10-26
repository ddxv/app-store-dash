<script lang="ts">
	import { run } from 'svelte/legacy';

	import { page } from '$app/stores';
	import { ListBox } from '@skeletonlabs/skeleton';

	import SideBarCatsListBoxItem from './SideBarCatsListBoxItem.svelte';


	import { homeCollectionSelection } from '../stores';
	let localHomeCollectionSelect = $homeCollectionSelection;
	// Reactive statement to update the store when localValue changes
	run(() => {
		homeCollectionSelection.set(localHomeCollectionSelect);
	});

	import { homeStoreSelection } from '../stores';
	let localHomeStoreSelect = $homeStoreSelection;
	run(() => {
		homeStoreSelection.set(localHomeStoreSelect);
	});

	import { homeCategorySelection } from '../stores';
	let localHomeCategorySelect = $state($homeCategorySelection);
	run(() => {
		homeCategorySelection.set(localHomeCategorySelect);
	});

	import type { CatData } from '../types';

	run(() => {
		if ($page.params.category) {
			localHomeCategorySelect = $page.params.category;
		}
	});

	interface Props {
		baseUrl: string;
		myCatData: CatData;
	}

	let { baseUrl, myCatData }: Props = $props();
</script>

<div class="p-1 md:p-2">
	<div class="card p-4">
		<h3 class="h4 md:h3">Categories</h3>
		<ListBox>
			{#if myCatData}
				{#each Object.entries(myCatData.categories) as [_prop, values]}
					{#if values.id && (Number(values.android) > 0 || values.name == 'Games')}
						{#if values.id != 'overall'}
							<a href="{baseUrl}/{values.id}">
								<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
							</a>
						{:else if baseUrl == '/companies/categories' && values.id == 'overall'}
							<a href="/companies">
								<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
							</a>
						{:else}
							<a href={baseUrl}>
								<SideBarCatsListBoxItem {values} {localHomeCategorySelect} />
							</a>
						{/if}
					{/if}
				{/each}
			{/if}
		</ListBox>
	</div>
</div>
