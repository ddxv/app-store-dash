<script lang="ts">
	import { page } from '$app/stores';
	import { Segment } from '@skeletonlabs/skeleton-svelte';
	import CardFirst from './CardFirst.svelte';
	import IconGoogle from '$lib/svg/IconGoogle.svelte';
	import IconiOS from '$lib/svg/IconiOS.svelte';
	import { homeCollectionSelection } from '../stores';
	import { homeStoreSelection } from '../stores';
	import { homeCategorySelection } from '../stores';

	import SideBarCatsListBoxItem from './SideBarCatsListBoxItem.svelte';

	import { storeIDLookup, collectionIDLookup, categoryIDLookup } from '../stores';

	const buttonSelectedClass =
		'bg-white border-2 border-primary-100 rounded-t-md relative top-[1px]';
	const buttonDeselectedClass = 'btn';
	const listClass = 'flex flex-col gap-2';

	let localHomeCollectionSelect = $homeCollectionSelection;
	let localHomeStoreSelect = $state($homeStoreSelection);
	let localHomeCategorySelect = $state($homeCategorySelection);
	import type { CatData } from '../types';

	// Function to generate a URL with existing query parameters
	function generateAdtechLink(storeName: string, adtechCategory: string) {
		const searchParams = $page.url.searchParams.toString();
		return `/adtech/${storeName}/${adtechCategory}${searchParams ? '?' + searchParams : ''}`;
	}

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
	let store_name = $derived($page.params.store_name);
	let adtech_category = $derived($page.params.type);
	// let company_category = $derived($page.params.category);
	// let company_name = $derived($page.params.name);
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
{/if}

{#if $page.url.pathname == '/rankings' || $page.url.pathname.startsWith('/rankings')}
	<div class="p-1 md:p-2">
		<CardFirst>
			{#snippet header()}
				<h4 class="h4 md:h3">Stores</h4>
			{/snippet}
			<nav class="list-nav">
				<ul>
					{#each Object.entries(storeIDLookup) as [_prop, values]}
						<li>
							<a
								href={`/rankings/store/${values.store_id}${
									values.store_id == 1
										? '/collection/1/category/1'
										: values.store_id == 2
											? '/collection/4/category/120'
											: '' // default value or path for other store_ids if needed
								}`}
								class={classesActive(`/rankings/store/${values.store_id}/`)}
							>
								{values.store_name}
							</a>
						</li>
					{/each}
				</ul>
			</nav>
		</CardFirst>
	</div>
	<div class="p-1 md:p-2">
		<CardFirst>
			{#snippet header()}
				<h4 class="md:h3 h4">Collections</h4>
			{/snippet}
			<nav class="list-nav">
				<ul>
					{#each Object.entries(collectionIDLookup[store]) as [id, values]}
						<li>
							<a
								href={`/rankings/store/${store}/collection/${values.collection_id}/category/${category}`}
								class={classesActive(
									`/rankings/store/${store}/collection/${values.collection_id}/`
								)}>{values.collection_name}</a
							>
						</li>
					{/each}
				</ul>
			</nav>
		</CardFirst>
	</div>
	<div class="p-1 md:p-2">
		<CardFirst>
			{#snippet header()}
				<h4 class="h4 md:h3">Categories</h4>
			{/snippet}
			<nav class="list-nav">
				<ul>
					{#each Object.entries(categoryIDLookup[collection]) as [id, values]}
						<li>
							<a
								href={`/rankings/store/${store}/collection/${collection}/category/${values.category_id}`}
								class={classesActive(
									`/rankings/store/${store}/collection/${collection}/category/${values.category_id}`
								)}>{values.category_name}</a
							>
						</li>
					{/each}
				</ul>
			</nav>
		</CardFirst>
	</div>
{/if}

{#if ($page.url.pathname.startsWith('/adtech') || $page.url.pathname.startsWith('/adtech')) && !$page.url.pathname.includes('companies')}
	<div class="p-1 md:p-2">
		<CardFirst>
			{#snippet header()}
				<h4 class="h4 md:h3">Stores</h4>
			{/snippet}
			<nav class="list-nav">
				<ul>
					{#each Object.entries(storeIDLookup) as [_prop, values]}
						<li>
							<a
								href={generateAdtechLink(values.store_name, adtech_category)}
								class={classesActive(`/adtech/${values.store_name}`)}
							>
								{values.store_name}
							</a>
						</li>
					{/each}
				</ul>
			</nav>
		</CardFirst>
	</div>

	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h3 class="h4 md:h3">Adtech Type</h3>
			<nav class="list-nav">
				<ul>
					<li>
						<a
							href={generateAdtechLink(store_name, 'networks')}
							class={classesActive('/adtech/Google/networks') ||
								classesActive('/adtech/Apple/networks')}>Advertising Networks</a
						>
					</li>
					<li>
						<a
							href={generateAdtechLink(store_name, 'trackers')}
							class={classesActive('/adtech/Google/trackers') ||
								classesActive('/adtech/Apple/trackers')}>Analytics, MMP Tracking and Attribution</a
						>
					</li>
				</ul>
			</nav>
		</div>
	</div>
	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h3 class="h4 md:h3">Categories</h3>
			<Segment
				name="collectionsCategories"
				bind:value={localHomeCategorySelect}
				orientation="vertical"
			>
				{#if myCatData}
					{#each Object.entries(myCatData.categories) as [_prop, values]}
						{#if values.id && (Number(values.android) > 0 || values.name == 'Games')}
							<Segment.Item value={values.id}
								><div class="flex w-full justify-between">
									<div class="flex-grow">
										{values.name}
									</div>
									{#if Number(values.android) > 0 || values.name == 'Games'}
										<div class="justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
										</div>
									{/if}
									{#if Number(values.ios) > 0}
										<div class="justify-end mr-2 md:mr-5">
											<IconiOS size="10" />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconiOS size="10" />
										</div>
									{/if}
								</div>
							</Segment.Item>
						{/if}
					{/each}
				{/if}
			</Segment>
		</div>
	</div>
{/if}
