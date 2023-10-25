<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar, TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import IconSearch from '$lib/IconSearch.svelte';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';

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

	$: classesActive = (href: string) => (href === $page.url.pathname ? buttonSelectedColor : '');

	export let data: Categories;

	import { myCategoryMap } from '../stores';
	import type { Categories } from '../types';
	myCategoryMap.set(data);

	function setCategorySelection(id: string) {
		localCategories = id;
	}
</script>

<!-- App Shell -->
<AppShell regionPage="p-8">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<a href="/" class="text-xl uppercase"><strong>App Store Data</strong></a>
			</svelte:fragment>
			<TabGroup
				justify="justify-start"
				active="variant-filled-primary"
				hover="hover:variant-soft-primary"
				flex="flex-1 lg:flex-none"
				rounded=""
				border=""
				class="bg-surface-100-800-token w-full"
			>
				<TabAnchor href="/" selected={$page.url.pathname === '/'}>
					<span>HOME</span>
				</TabAnchor>
				<TabAnchor href="/about" selected={$page.url.pathname === '/about'}>
					<span>ABOUT</span>
				</TabAnchor>
			</TabGroup>
			<svelte:fragment slot="trail">
				<div class="input-group grid-cols-[auto_1fr_auto]">
					<div class="input-group-shim">
						<IconSearch />
					</div>
					<input type="search" placeholder=" Apps..." />
				</div>

				<TabGroup
					justify="justify-end"
					active="variant-filled-primary"
					hover="hover:variant-soft-primary"
					flex="flex-1 lg:flex-none"
					rounded=""
					border=""
					class="bg-surface-100-800-token w-full"
				>
					<TabAnchor href="https://ads.jamesoclaire.com/dash/ads">
						<span>Ads.txt Dash</span>
					</TabAnchor>
					<TabAnchor href="https://jamesoclaire.com">
						<span>Blog</span>
					</TabAnchor>
				</TabGroup>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		{#if $page.url.pathname == '/' || $page.url.pathname.startsWith('/collections')}
			<br />
			<div class="p-2">
				<h4 class="h4">List</h4>
				<div class="card variant-glass-surface p-4 text-token">
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
				<h4 class="h4">Stores</h4>
				<div class=" card variant-glass-surface p-4 text-token">
					<ListBox>
						<ListBoxItem
							bind:group={localMyStore}
							name="medium"
							value="google"
							active={buttonSelectedColor}>Google</ListBoxItem
						>
						<ListBoxItem
							bind:group={localMyStore}
							name="medium"
							value="ios"
							active={buttonSelectedColor}>Apple</ListBoxItem
						>
					</ListBox>
				</div>
				<br />

				<h4 class="h4">Categories</h4>
				<div class=" card variant-glass-surface p-4 text-token">
					<ListBox>
						{#if data}
							{#each Object.entries(data.mycats.categories) as [_prop, values]}
								{#if values.id}
									<ListBoxItem
										bind:group={localCategories}
										name="medium"
										value={values.id}
										active={buttonSelectedColor}>{values.name}</ListBoxItem
									>
								{/if}
							{/each}
						{/if}
					</ListBox>
				</div>
			</div>

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
		<!-- --- -->
	</svelte:fragment>
	<slot />
	<!-- Page Route Content -->
</AppShell>
