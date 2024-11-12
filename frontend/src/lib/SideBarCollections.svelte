<script lang="ts">
	import { page } from '$app/stores';
	import CardFirst from './CardFirst.svelte';
	import { homeCollectionSelection } from '../stores';
	import { homeStoreSelection } from '../stores';
	import { homeCategorySelection } from '../stores';

	const buttonSelectedClass =
		'preset-filled-primary border-2 border-primary-100 rounded-t-md relative top-[1px]';
	const buttonDeselectedClass = 'btn';
	const listClass = 'flex flex-col gap-2';

	let localHomeCollectionSelect = $homeCollectionSelection;
	let localHomeStoreSelect = $state($homeStoreSelection);
	let localHomeCategorySelect = $state($homeCategorySelection);
	import type { CatData } from '../types';

	// FOLOWING IS FOR RANKINGS

	interface Props {
		myCatData: CatData;
	}

	let { myCatData }: Props = $props();

	let classesActive = $derived((href: string) =>
		$page.url.pathname.startsWith(href) ? buttonSelectedClass : buttonDeselectedClass
	);

	let classesActiveStore = $derived((store: string) =>
		localHomeStoreSelect == store ? buttonSelectedClass : buttonDeselectedClass
	);

	let classesActiveCategory = $derived((category: string) =>
		localHomeCategorySelect == category ? buttonSelectedClass : buttonDeselectedClass
	);

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

<div class="p-1 md:p-2">
	<CardFirst>
		{#snippet header()}
			<h3 class="h4 md:h3">Appstores</h3>
		{/snippet}
		<div class={listClass}>
			<button
				class={classesActiveStore('google')}
				value="google"
				onclick={() => (localHomeStoreSelect = 'google')}>Google</button
			>
			<button
				class={classesActiveStore('ios')}
				value="ios"
				onclick={() => (localHomeStoreSelect = 'ios')}>Apple</button
			>
		</div>
	</CardFirst>
</div>

<div class="p-1 md:p-2">
	<CardFirst>
		{#snippet header()}
			<h3 class="h3">Time</h3>
		{/snippet}
		<div class={listClass}>
			<a href="/collections/new_yearly" class={classesActive('/collections/new_yearly')}
				>New this Year</a
			>
			<a href="/collections/new_monthly" class={classesActive('/collections/new_monthly')}
				>New this Month</a
			>
			<a href="/collections/new_weekly" class={classesActive('/collections/new_weekly')}
				>New this Week</a
			>
			<a href="/collections/top" class={classesActive('/collections/top')}>Alltime Top</a>
		</div>
	</CardFirst>
</div>

<div class="p-1 md:p-2">
	<CardFirst>
		{#snippet header()}
			<h3 class="h3">Appstore Categories</h3>
		{/snippet}
		<div class={listClass}>
			{#if myCatData}
				{#each Object.entries(myCatData.categories) as [_prop, values]}
					{#if values.id && values.name != 'Overview'}
						<button
							class={classesActiveCategory(values.id)}
							value={values.id}
							onclick={() => (localHomeCategorySelect = values.id)}>{values.name}</button
						>
					{/if}
				{/each}
			{/if}
		</div>
	</CardFirst>
</div>
