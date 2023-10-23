<script>
	import '../app.postcss';
	import { AppShell, AppBar, TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import IconSearch from '$lib/IconSearch.svelte';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';

	import { myListSelectionStore } from '../stores';
	let localMyList = $myListSelectionStore;
	// Reactive statement to update the store when localValue changes
	$: myListSelectionStore.set(localMyList);

	import { myStoreSelection } from '../stores';
	let localMyStore = $myStoreSelection;
	$: myStoreSelection.set(localMyStore);

	let myCategories = ['books'];
	export let data;
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
					<TabAnchor href="https://ads.jamesoclaire.com">
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
		{#if $page.url.pathname == '/'}
			<div class="p-2">
				<br />
				<h4 class="h4">List</h4>
				<div class=" card p-4 text-token">
					<ListBox>
						<ListBoxItem bind:group={localMyList} name="medium" value="new_weekly"
							>New this Week by Downloads</ListBoxItem
						>
						<ListBoxItem bind:group={localMyList} name="medium" value="new_monthly"
							>New this Month by Downloads</ListBoxItem
						>
					</ListBox>
				</div>

				<br />
				<h4 class="h4">Stores</h4>
				<div class=" card p-4 text-token">
					<ListBox>
						<ListBoxItem bind:group={localMyStore} name="medium" value="google">Google</ListBoxItem>
						<ListBoxItem bind:group={localMyStore} name="medium" value="ios">Apple</ListBoxItem>
					</ListBox>
				</div>
				<br />
				<h4 class="h4">Categories</h4>
				<div class=" card p-4 text-token">
					<ListBox multiple>
						{#if data}
							{#each Object.entries(data.mycats.categories) as [_prop, values]}
								{#if values.id}
									<ListBoxItem bind:group={myCategories} name="medium" value="${values.id}"
										>{values.name}</ListBoxItem
									>
								{/if}
							{/each}
						{/if}
					</ListBox>
				</div>
			</div>
		{/if}
		<!-- --- -->
	</svelte:fragment>
	<slot />
	<!-- Page Route Content -->
</AppShell>
