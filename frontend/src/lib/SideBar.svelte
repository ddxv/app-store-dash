<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';

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

	import type { CatData } from '../types';
	export let myCatData: CatData;

	const scrollTop = () => {
		const elemPage = document.querySelector('#page');
		if (elemPage !== null) {
			elemPage.scrollTop = 0;
		}
	};

	// For adtech
	$: store_name = $page.params.store_name;
	$: adtech_category = $page.params.type;

	// FOLOWING IS FOR RANKINGS

	import { storeIDLookup, collectionIDLookup, categoryIDLookup } from '../stores';

	$: store = +$page.params.store;
	$: collection = +$page.params.collection;
	$: category = +$page.params.category;

	// Logic to adjust collection and category based on the store's value
	$: {
		// If store is not a number (NaN), default it to 1
		if (isNaN(store)) {
			store = 1;
		}

		switch (store) {
			case 2:
				collection = 4;
				category = 55;
				break;
			case 1:
			default: // Defaults for store=1 or any other value not explicitly handled
				collection = 1;
				category = 1;
				break;
		}
	}
</script>

{#if $page.url.pathname.startsWith('/collections')}
	<div class="p-1 md:p-2">
		<div class=" card p-4 text-token">
			<h3 class="h4 md:h3">Stores</h3>
			<ListBox>
				<ListBoxItem
					bind:group={localHomeStoreSelect}
					name="medium"
					value="google"
					padding="p-2 md:p-2"
					on:click={scrollTop}
					active={buttonSelectedColor}>Google</ListBoxItem
				>
				<ListBoxItem
					bind:group={localHomeStoreSelect}
					name="medium"
					on:click={scrollTop}
					value="ios"
					padding="p-2 md:p-2"
					active={buttonSelectedColor}>Apple</ListBoxItem
				>
			</ListBox>
		</div>
	</div>

	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h3 class="h3">Top New Apps</h3>
			<nav class="list-nav">
				<ul>
					<li>
						<a href="/collections/new_yearly" class={classesActive('/collections/new_yearly')}
							>New this Year</a
						>
					</li>
					<li>
						<a href="/collections/new_monthly" class={classesActive('/collections/new_monthly')}
							>New this Month</a
						>
					</li>
					<li>
						<a href="/collections/new_weekly" class={classesActive('/collections/new_weekly')}
							>New this Week</a
						>
					</li>
					<li>
						<a href="/collections/top" class={classesActive('/collections/top')}>Alltime Top</a>
					</li>
				</ul>
			</nav>
		</div>
	</div>

	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h3 class="h3">Categories</h3>
			<ListBox>
				{#if myCatData}
					{#each Object.entries(myCatData.categories) as [_prop, values]}
						{#if values.id}
							<ListBoxItem
								bind:group={localHomeCategorySelect}
								name="medium"
								value={values.id}
								active={buttonSelectedColor}
								on:click={scrollTop}
								padding="p-2 md:p-2"
								><div class="flex w-full justify-between">
									<div class="flex-grow">
										{values.name}
									</div>

									{#if Number(values.android) > 0}
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
							</ListBoxItem>
						{/if}
					{/each}
				{/if}
			</ListBox>
		</div>
	</div>
{/if}

{#if $page.url.pathname == '/rankings' || $page.url.pathname.startsWith('/rankings')}
	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h4 class="h4 md:h3">Stores</h4>
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
	</div>
	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h4 class="md:h3 h4">Collections</h4>
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
		</div>
	</div>
	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h4 class="h4 md:h3">Categories</h4>
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
	</div>
{/if}

{#if ($page.url.pathname.startsWith('/adtech') || $page.url.pathname.startsWith('/adtech')) && !$page.url.pathname.includes('companies')}
	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h4 class="h4 md:h3">Stores</h4>
			<nav class="list-nav">
				<ul>
					{#each Object.entries(storeIDLookup) as [_prop, values]}
						<li>
							<a
								href={`/adtech/${values.store_name}/${adtech_category}`}
								class={classesActive(`/adtech/${values.store_name}`)}
							>
								{values.store_name}
							</a>
						</li>
					{/each}
				</ul>
			</nav>
		</div>
	</div>

	<div class="p-1 md:p-2">
		<div class="card p-4">
			<h3 class="h4 md:h3">Adtech Type</h3>
			<nav class="list-nav">
				<ul>
					<li>
						<a
							href={`/adtech/${store_name}/networks`}
							class={classesActive('/adtech/Google/networks') ||
								classesActive('/adtech/Apple/networks')}>Advertising Networks</a
						>
					</li>
					<li>
						<a
							href={`/adtech/${store_name}/trackers`}
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
			<ListBox>
				{#if myCatData}
					{#each Object.entries(myCatData.categories) as [_prop, values]}
						{#if values.id && (Number(values.android) > 0 || values.name == 'Games')}
							<ListBoxItem
								bind:group={localHomeCategorySelect}
								name="medium"
								value={values.id}
								active={buttonSelectedColor}
								on:click={scrollTop}
								padding="p-2 md:p-2"
								><div class="flex w-full justify-between">
									<div class="flex-grow">
										{values.name}
									</div>
									{#if Number(values.android) > 0}
										<div class="justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
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
