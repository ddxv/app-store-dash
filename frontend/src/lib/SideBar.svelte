<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	// $: classesActive = (href: string) => (href === $page.url.pathname ? buttonSelectedColor : '');
	$: classesActive = (href: string) =>
		$page.url.pathname.startsWith(href) ? buttonSelectedColor : '';

	import IconGoogle from '$lib/svg/IconGoogle.svelte';
	import IconiOS from '$lib/svg/IconiOS.svelte';

	import { homeCollectionSelection } from '../stores';
	let localHomeCollectionSelect = $homeCollectionSelection;
	// Reactive statement to update the store when localValue changes
	$: homeCollectionSelection.set(localHomeCollectionSelect);

	import { homeStoreSelection } from '../stores';
	let localHomeStoreSelect = $homeStoreSelection;
	$: homeStoreSelection.set(localHomeStoreSelect);

	import { homeCategorySelection } from '../stores';
	let localHomeCategorySelect = $homeCategorySelection;
	const buttonSelectedColor = 'bg-gradient-to-tl variant-gradient-primary-secondary text-white';
	$: homeCategorySelection.set(localHomeCategorySelect);

	import type { CategoriesInfo } from '../types';
	export let data: CategoriesInfo;

	// import { getDrawerStore } from '@skeletonlabs/skeleton';

	// const drawerStore = getDrawerStore();

	// function drawerClose(): void {
	// 	drawerStore.close();
	// }

	// FOLOWING IS FOR RANKINGS

	import { storeIDLookup, collectionIDLookup, categoryIDLookup } from '../stores';

	$: store = +$page.params.store;
	$: collection = +$page.params.collection;
	$: category = +$page.params.category;

	$: {
		if (store == 2) {
			collection = 4;
			category = 55;
		}
		if (store == 1) {
			collection = 1;
			category = 1;
		}
	}
</script>

{#if $page.url.pathname == '/' || $page.url.pathname.startsWith('/collections')}
	<div class="p-1 md:p-2">
		<div class="card variant-glass-surface p-4">
			<h4 class="h4">Collections</h4>
			<nav class="list-nav">
				<ul>
					<li>
						<a href="/collections/top" class={classesActive('/collections/top')}>Alltime Top</a>
					</li>
					<li>
						<a href="/collections/new_yearly" class={classesActive('/collections/new_yearly')}
							>New this Year by Downloads</a
						>
					</li>
					<li>
						<a href="/collections/new_monthly" class={classesActive('/collections/new_monthly')}
							>New this Month by Downloads</a
						>
					</li>

					<li>
						<a href="/collections/new_weekly" class={classesActive('/collections/new_weekly')}
							>New this Week by Downloads</a
						>
					</li>
				</ul>
			</nav>
		</div>

		<br />
		<div class=" card variant-glass-surface p-2 md:p-4 text-token">
			<h4 class="h4">Stores</h4>
			<ListBox>
				<ListBoxItem
					bind:group={localHomeStoreSelect}
					name="medium"
					value="Google"
					padding="p-2 md:p-2"
					active={buttonSelectedColor}>Google</ListBoxItem
				>
				<ListBoxItem
					bind:group={localHomeStoreSelect}
					name="medium"
					value="ios"
					padding="p-2 md:p-2"
					active={buttonSelectedColor}>Apple</ListBoxItem
				>
			</ListBox>
		</div>
		<br />

		<div class="card variant-glass-surface p-2 md:p-4 text-token">
			<h4 class="h4">Categories</h4>
			<ListBox>
				{#if data}
					{#each Object.entries(data.mycats.categories) as [_prop, values]}
						{#if values.id}
							<ListBoxItem
								bind:group={localHomeCategorySelect}
								name="medium"
								value={values.id}
								active={buttonSelectedColor}
								padding="p-2 md:p-2"
								><div class="flex w-full justify-between">
									<div class="flex-grow">
										{values.name}
									</div>

									{#if Number(values.android) > 0}
										<div class="justify-end mr-2 md:mr-5">
											<IconGoogle />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconGoogle />
										</div>
									{/if}
									{#if Number(values.ios) > 0}
										<div class="justify-end mr-2 md:mr-5">
											<IconiOS />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconiOS />
										</div>
									{/if}
								</div>
							</ListBoxItem>
						{/if}
					{/each}
				{/if}
			</ListBox>
		</div>
	</div>
{/if}

{#if $page.url.pathname == '/rankings' || $page.url.pathname.startsWith('/rankings')}
	<div class="card variant-glass-surface p-4">
		<h4 class="h4">Stores</h4>
		<nav class="list-nav">
			<ul>
				{#each Object.entries(storeIDLookup) as [_prop, values]}
					<li>
						<a
							href={`/rankings/store/${values.store_id}${
								values.store_id == 1
									? '/collection/1/category/1'
									: values.store_id == 2
									? '/collection/4/category/55'
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
	</div>
	<div class="card variant-glass-surface p-4">
		<h4 class="h4">Collections</h4>
		<nav class="list-nav">
			<ul>
				{#each Object.entries(collectionIDLookup[store]) as [id, values]}
					<li>
						<a
							href={`/rankings/store/${store}/collection/${values.collection_id}/category/${category}`}
							class={classesActive(`/rankings/store/${store}/collection/${values.collection_id}/`)}
							>{values.collection_name}</a
						>
					</li>
				{/each}
			</ul>
		</nav>
	</div>
	<div class="card variant-glass-surface p-4">
		<h4 class="h4">Categories</h4>
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
	</div>
{/if}
