<script lang="ts">
	import '../app.postcss';
	import {
		AppShell,
		AppBar,
		initializeStores,
		Drawer,
		getDrawerStore,
		type DrawerSettings
	} from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import IconSearch from '$lib/svg/IconSearch.svelte';
	import type { AfterNavigate } from '@sveltejs/kit';
	import { afterNavigate } from '$app/navigation';

	let searchTerm: string;

	function navigateToSearch(event: any) {
		if (event.key === 'Enter' && searchTerm.trim() !== '') {
			// Replace spaces with '+'
			const encodedSearchTerm = encodeURIComponent(searchTerm.replace(/\s+/g, '+'));

			// Navigate to the search route
			window.location.href = `/search/${encodedSearchTerm}`;
		}
	}

	import { homeCategoryMap } from '../stores';
	import type { CategoriesInfo } from '../types';
	export let data: CategoriesInfo;
	homeCategoryMap.set(data);

	import SideBar from '$lib/SideBar.svelte';
	import NavTabs from '$lib/NavTabs.svelte';
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
		drawerStore.open(drawerSettings);
	};

	// Scroll to top after navigation
	afterNavigate((params: AfterNavigate) => {
		const isNewPage: boolean = params.from?.route.id !== params.to?.route.id;
		const elemPage = document.querySelector('#page');
		if (isNewPage && elemPage !== null) {
			elemPage.scrollTop = 0;
		}
	});
</script>

<Drawer>
	{#await data.mycats.streamed then data}
		<SideBar myCatData={data} />
	{/await}
</Drawer>

<!-- App Shell -->
<AppShell
	regionPage="p-2 md:p-8"
	slotSidebarLeft="w-0 lg:w-auto"
	slotPageHeader="hidden lg:inline-flex"
>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar
			gridColumns="grid-cols-[1fr_0_1fr] md:grid-cols-[0.4fr_1fr_0.3fr]"
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

			<div class="hidden lg:inline-flex">
				<NavTabs />
			</div>

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
		{#await data.mycats.streamed then myCatData}
			<SideBar {myCatData} />
		{/await}
	</svelte:fragment>

	<svelte:fragment slot="footer">
		{#if $page.url.pathname == '/' || $page.url.pathname.startsWith('/collections') || $page.url.pathname.startsWith('/rankings')}
			<AppBar
				slotLead="p-0"
				slotTrail="p-2"
				spacing="space-y-0"
				padding="p-0"
				gap="gap-0"
				class=" bg-gradient-to-tr from-indigo-500/50 via-purple-500/50 to-pink-500/50 lg:hidden"
				gridColumns="grid-cols-[auto_1fr_auto]"
			>
				<svelte:fragment slot="lead">
					<div class="inline-flex">
						<NavTabs />
					</div>
				</svelte:fragment>

				<svelte:fragment slot="trail">
					<button class="lg:hidden btn flex mr-2 pl-0" on:click={drawerOpen}>
						<h4 class="h4">FILTERS</h4>
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
