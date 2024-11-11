<script lang="ts">
	import {
		// Drawer,
		// initializeStores,
		// getDrawerStore,
		type DrawerSettings
	} from '@skeletonlabs/skeleton';

	import { homeCategoryMap } from '../../stores';
	import type { CategoriesInfo } from '../../types';
	import SideBar from '$lib/SideBar.svelte';

	interface Props {
		data: CategoriesInfo;
		children?: import('svelte').Snippet;
	}

	let { data, children }: Props = $props();
	homeCategoryMap.set(data);

	// initializeStores();
	// const drawerStore = getDrawerStore();

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
		// drawerStore.open(drawerSettings);
	};
</script>

<!-- <Drawer>
	{#await data.appCats then data}
		<SideBar myCatData={data} />
	{/await}
</Drawer> -->

<div class="grid grid-cols-1 md:grid-cols-[auto_1fr]">
	<aside>
		{#await data.appCats then myCatData}
			<SideBar {myCatData} />
		{/await}
	</aside>
	{@render children?.()}
	<button
		class="lg:hidden btn preset-filled-primary absolute right-[20px] bottom-[50px]"
		onclick={drawerOpen}
	>
		<h4 class="h4">FILTERS</h4>
		<span>
			<svg viewBox="0 0 100 80" class="fill w-4 h-4">
				<rect width="100" height="20" />
				<rect y="30" width="100" height="20" />
				<rect y="60" width="100" height="20" />
			</svg>
		</span>
	</button>
</div>
