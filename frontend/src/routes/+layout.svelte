<script lang="ts">
	import '../app.postcss';
	import {
		AppShell,
		AppBar,
		TabGroup,
		TabAnchor,
		initializeStores,
		Drawer,
		getDrawerStore,
		type DrawerSettings
	} from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import IconSearch from '$lib/svg/IconSearch.svelte';

	let searchTerm: string;

	function navigateToSearch(event: any) {
		if (event.key === 'Enter' && searchTerm.trim() !== '') {
			// Replace spaces with '+'
			const encodedSearchTerm = encodeURIComponent(searchTerm.replace(/\s+/g, '+'));

			// Navigate to the search route
			window.location.href = `/search/${encodedSearchTerm}`;
		}
	}

	import { myCategoryMap } from '../stores';
	import type { CategoriesInfo } from '../types';
	export let data: CategoriesInfo;
	myCategoryMap.set(data);

	import SideBar from '$lib/SideBar.svelte';
	initializeStores();
	const drawerStore = getDrawerStore();

	const drawerSettings: DrawerSettings = {
		id: 'example-3',
		// Provide your property overrides:
		// bgDrawer: 'bg-purple-900 text-white',
		bgDrawer: 'bg-gradient-to-tr from-indigo-100/50 via-purple-500/75 to-pink-100',
		bgBackdrop: 'bg-gradient-to-tr from-indigo-500/10 via-purple-500/10 to-pink-500/10',
		width: 'w-[280px] md:w-[480px] h-[580px]',
		padding: 'p-0',
		rounded: 'rounded-xl',
		position: 'bottom'
	};

	const drawerOpen = () => {
		console.log('OPEN!');
		drawerStore.open(drawerSettings);
	};

	console.log('hi');
</script>

<Drawer>
	<SideBar {data} />
</Drawer>

<!-- App Shell -->
<AppShell
	regionPage="p-2 md:p-8"
	slotSidebarLeft="w-0 lg:w-auto"
	slotPageHeader="hidden md:inline-flex"
>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar
			gridColumns="grid-cols-[1fr_1fr_1fr]"
			slotLead="p-2"
			slotTrail="p-2"
			spacing="space-y-0"
			padding="p-0"
			class="bg-gradient-to-tr from-indigo-500/50 via-purple-500/50 to-pink-500/50"
		>
			<svelte:fragment slot="lead">
				<div class="flex items-center">
					<a class="flex" href="/">
						<!-- <img class="h-8 m w-8 md:h-12 md:w-12" src="/cute_eyes_250.png" alt="Goblin Icon" /> -->
						<img
							class="ml-2 h-8 m w-8 md:h-12 md:w-12"
							src="/goblin_purple_hat_250.png"
							alt="Goblin Icon"
						/>
						<strong class="tex-xl ml-2 md:text-2xl uppercase">AppGoblin</strong>
					</a>
				</div>
			</svelte:fragment>

			<TabGroup
				active="variant-filled-primary"
				hover="hover:variant-soft-primary"
				flex="flex-1"
				rounded=""
				border=""
				class=" w-full p-0 hidden md:inline-flex"
			>
				<TabAnchor class="p-0 px-0" href="/" selected={$page.url.pathname === '/'}>HOME</TabAnchor>
				<TabAnchor href="/categories" selected={$page.url.pathname === '/categories'}
					>CATEGORIES
				</TabAnchor>
				<TabAnchor href="/about" selected={$page.url.pathname === '/about'}>ABOUT</TabAnchor>
			</TabGroup>

			<svelte:fragment slot="trail">
				<div class="input-group grid-cols-2 sm:grid-cols-[50px_auto]">
					<div class="input-group-shim p-1 md:p-3">
						<IconSearch />
					</div>
					<input
						type="search"
						bind:value={searchTerm}
						on:keydown={navigateToSearch}
						placeholder="Search"
						class="p-1 md:p-3"
					/>
				</div>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<SideBar {data} />
	</svelte:fragment>

	<svelte:fragment slot="footer">
		{#if $page.url.pathname == '/' || $page.url.pathname.startsWith('/collections')}
			<AppBar
				slotLead="p-2"
				slotTrail="p-2"
				spacing="space-y-0"
				padding="p-0"
				class="bg-gradient-to-tr from-indigo-500/50 via-purple-500/50 to-pink-500/50 lg:hidden"
			>
				<svelte:fragment slot="trail">
					<button class="lg:hidden btn btn-md ml-auto mr-2" on:click={drawerOpen}>
						<span>
							<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
								<rect width="100" height="20" />
								<rect y="30" width="100" height="20" />
								<rect y="60" width="100" height="20" />
							</svg>
						</span>
					</button>
				</svelte:fragment>
			</AppBar>
		{/if}
	</svelte:fragment>

	<slot />
	<!-- Page Route Content -->
</AppShell>
