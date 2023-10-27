<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	$: classesActive = (href: string) => (href === $page.url.pathname ? buttonSelectedColor : '');

	import IconGoogle from '$lib/svg/IconGoogle.svelte';
	import IconiOS from '$lib/svg/IconiOS.svelte';

	import { myCollectionStore } from '../stores';
	let localMyList = $myCollectionStore;
	// Reactive statement to update the store when localValue changes
	$: myCollectionStore.set(localMyList);

	import { myStoreSelection } from '../stores';
	let localMyStore = $myStoreSelection;
	$: myStoreSelection.set(localMyStore);

	import { myCategorySelection } from '../stores';
	let localCategories = $myCategorySelection;
	const buttonSelectedColor = 'bg-gradient-to-tl variant-gradient-primary-secondary text-white';
	$: myCategorySelection.set(localCategories);

	function setCategorySelection(id: string) {
		localCategories = id;
		window.location.href = `/categories/${id}`;
	}
	import type { CategoriesInfo } from '../types';
	export let data: CategoriesInfo;
	import { myCategoryMap } from '../stores';

	// import { getDrawerStore } from '@skeletonlabs/skeleton';

	// const drawerStore = getDrawerStore();

	// function drawerClose(): void {
	// 	drawerStore.close();
	// }
</script>

{#if $page.url.pathname == '/' || $page.url.pathname.startsWith('/collections')}
	<div class="p-1 md:p-2">
		<div class="card variant-glass-surface p-4">
			<h4 class="h4">List</h4>
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
					bind:group={localMyStore}
					name="medium"
					value="google"
					padding="p-2 md:p-2"
					active={buttonSelectedColor}>Google</ListBoxItem
				>
				<ListBoxItem
					bind:group={localMyStore}
					name="medium"
					value="ios"
					padding="p-2 md:p-2"
					active={buttonSelectedColor}>Apple</ListBoxItem
				>
			</ListBox>
		</div>
		<br />

		<div class=" card variant-glass-surface p-2 md:p-4 text-token">
			<h4 class="h4">Categories</h4>
			<ListBox>
				{#if data}
					{#each Object.entries(data.mycats.categories) as [_prop, values]}
						{#if values.id}
							<ListBoxItem
								bind:group={localCategories}
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

{#if $page.url.pathname == '/categories' || $page.url.pathname.startsWith('/categories')}
	<h4 class="h4">Categories TABLE</h4>
	{#if $myCategoryMap}
		<!-- Responsive Container (recommended) -->
		<div class="table-container">
			<!-- Native Table Element -->
			<table class="table table-hover table-interactive table-compact">
				<thead>
					<tr>
						<th>Category</th>
						<th>Android</th>
						<th>iOS</th>
					</tr>
				</thead>
				<tbody>
					{#each Object.entries($myCategoryMap.mycats.categories) as [_i, row]}
						{#if row.id == localCategories}
							<tr class="table-row-checked" on:click={() => setCategorySelection(row.id)}>
								<td>{row.name}</td>
								<td>{row.android}</td>
								<td>{row.ios}</td>
							</tr>
						{:else}
							<tr on:click={() => setCategorySelection(row.id)}>
								<td>{row.name}</td>
								<td>{row.android}</td>
								<td>{row.ios}</td>
							</tr>
						{/if}
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
{/if}
