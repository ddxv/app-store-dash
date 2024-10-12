<script lang="ts">
	import {
		AppShell,
		Drawer,
		initializeStores,
		getDrawerStore,
		type DrawerSettings
	} from '@skeletonlabs/skeleton';

	import { homeCategoryMap } from '../../stores';
	import type { CategoriesInfo } from '../../types';
	import NewSideBar from '$lib/SideBarNew.svelte';
	export let data: CategoriesInfo;
	homeCategoryMap.set(data);

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
		console.log('clicked drawer');
		drawerStore.open(drawerSettings);
	};
</script>

<Drawer>
	{#await data.mycats then data}
		<NewSideBar myCatData={data} />
	{/await}
</Drawer>

<AppShell slotSidebarLeft="w-0 lg:w-auto">
	<svelte:fragment slot="sidebarLeft">
		{#await data.mycats then myCatData}
			<NewSideBar {myCatData} />
		{/await}
	</svelte:fragment>
	<slot />
	<button
		class="lg:hidden btn variant-filled-primary absolute right-[20px] bottom-[50px]"
		on:click={drawerOpen}
	>
		<h4 class="h4">FILTERS</h4>
		<span>
			<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
				<rect width="100" height="20" />
				<rect y="30" width="100" height="20" />
				<rect y="60" width="100" height="20" />
			</svg>
		</span>
	</button>
</AppShell>
