<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	$: classesActive = (href: string) => (href === $page.url.pathname ? buttonSelectedColor : '');

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

	import { RadioGroup, RadioItem } from '@skeletonlabs/skeleton';
	// import { getDrawerStore } from '@skeletonlabs/skeleton';

	// const drawerStore = getDrawerStore();

	// function drawerClose(): void {
	// 	drawerStore.close();
	// }

	// FOLOWING IS FOR RANKINGS
	// import { myStoreRankingsMap } from '../stores';

	import { storeIDLookup, collectionIDLookup, categoryIDLookup } from '../stores';

	import { idStoreSelection } from '../stores';
	let localIDStoreSelect = $idStoreSelection;
	$: idStoreSelection.set(localIDStoreSelect);
	$: {
		idStoreSelection.set(localIDStoreSelect);
		if (localIDStoreSelect == 1) {
			localIDCollectionSelect = 1;
		} else {
			localIDCollectionSelect = 4;
		}
	}

	import { idCollectionSelection } from '../stores';
	let localIDCollectionSelect = $idCollectionSelection;
	$: idCollectionSelection.set(localIDCollectionSelect);
	$: {
		idCollectionSelection.set(localIDCollectionSelect);
		if (localIDCategorySelect < 55) {
			if (localIDCollectionSelect >= 4) {
				localIDCategorySelect = 55;
			} else {
				localIDCategorySelect = 1;
			}
		}
	}

	import { idCategorySelection } from '../stores';
	let localIDCategorySelect = $idCategorySelection;

	$: idCategorySelection.set(localIDCategorySelect);
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
					value="google"
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
	<div class="p-1 md:p-2">
		<div class="card variant-glass-surface p-4">
			<h4 class="h4">Stores</h4>
			<RadioGroup rounded="rounded-container-token" display="flex-col">
				{#each Object.entries(storeIDLookup) as [_prop, values]}
					<RadioItem bind:group={localIDStoreSelect} name="justify" value={values.store_id}
						>{values.store_name}</RadioItem
					>
				{/each}
			</RadioGroup>
		</div>
	</div>

	<div class="p-1 md:p-2">
		<div class="card variant-glass-surface p-4">
			<h4 class="h4">Collections</h4>
			{#if !(localIDCollectionSelect in collectionIDLookup[localIDStoreSelect])}
				setFromTS={localIDCollectionSelect}
				setFromHTML={parseInt(Object.keys(collectionIDLookup[localIDStoreSelect])[0])}
			{/if}
			<RadioGroup rounded="rounded-container-token" display="flex-col">
				{#each Object.entries(collectionIDLookup[localIDStoreSelect]) as [id, values]}
					<RadioItem
						bind:group={localIDCollectionSelect}
						name="justify"
						value={values.collection_id}>{values.collection_name}</RadioItem
					>
				{/each}
			</RadioGroup>
		</div>
	</div>

	<div class="p-1 md:p-2">
		<div class="card variant-glass-surface p-4">
			<h4 class="h4">Categories</h4>
			<RadioGroup rounded="rounded-container-token" display="flex-col">
				{#each Object.entries(categoryIDLookup[localIDCollectionSelect]) as [id, values]}
					<RadioItem bind:group={localIDCategorySelect} name="justify" value={values.category_id}
						>{values.category_name}, {values.category_id}</RadioItem
					>
				{/each}
			</RadioGroup>
		</div>
	</div>
{/if}
