<script lang="ts">
	import '../app.css';
	import { page } from '$app/stores';

	import IconSearch from '$lib/svg/IconSearch.svelte';
	import OpenSideBarDrawer from '$lib/utils/OpenSideBarDrawer.svelte';
	import SideBar from '$lib/SideBar.svelte';

	import { AppBar } from '@skeletonlabs/skeleton-svelte';

	import { homeCategoryMap } from '../stores';

	import githubIcon from '$lib/svg/github-mark.svg?raw';
	import discordIcon from '$lib/svg/discord-mark-black.svg?raw';

	let searchTerm: string = $state('');

	function navigateToSearch(event: any) {
		if (event.key === 'Enter' && searchTerm.trim() !== '') {
			// Replace spaces with '+'
			const encodedSearchTerm = encodeURIComponent(searchTerm.replace(/\s+/g, '+'));

			// Navigate to the search route
			window.location.href = `/search/${encodedSearchTerm}`;
		}
	}

	import NavTabs from '$lib/NavTabs.svelte';
	interface Props {
		data;
		children?: import('svelte').Snippet;
	}

	let { data, children }: Props = $props();

	homeCategoryMap.set(data.appCats);
</script>

<div class="grid h-screen grid-rows-[auto_1fr_auto]">
	<header class="sticky top-0 z-10">
		<AppBar
			leadBase="mr-2"
			trailBase="mx-2 my-1"
			padding="p-1 md:px-2 md:py-1"
			centerBase="hidden md:block"
			background="bg-surface-50-950"
		>
			{#snippet lead()}
				<div class="flex items-center">
					<a class="flex" href="/">
						<img
							class="md:ml-2 h-8 md:h-12 w-8 md:w-12"
							src="/goblin_purple_hat_250.png"
							alt="Goblin Icon"
						/>
						<strong class="text-xl ml-1 md:ml-2 md:text-3xl uppercase text-primary-900-100"
							>AppGoblin</strong
						>
					</a>
				</div>
			{/snippet}

			<div class="hidden md:inline-flex">
				<NavTabs />
			</div>

			{#snippet trail()}
				<div>
					<div class="input-group grid-cols-2 grid-cols-[auto_1fr]">
						<div class="input-group-shim p-1 md:p-2">
							<IconSearch />
						</div>
						<div class="text-xs md:text-lg p-1">
							<input
								type="search"
								bind:value={searchTerm}
								onkeydown={navigateToSearch}
								placeholder="Search Apps & Companies"
								class="p-0"
							/>
						</div>
					</div>
					<div class="flex items-center p-1 gap-2">
						<a href="https://github.com/ddxv/app-store-dash" target="_blank" rel="noreferrer">
							<button type="button" class="btn preset-tonal hover:preset-tonal-primary p-2">
								<div class="inline-flex items-center text-xs md:text-lg gap-2">
									{@html githubIcon} GitHub
								</div>
							</button>
						</a>

						<a href="https://discord.gg/7jpWEhkXRW" target="_blank" rel="noreferrer">
							<button type="button" class="btn preset-tonal hover:preset-tonal-primary p-2">
								<div class="inline-flex items-center text-xs md:text-lg gap-2">
									{@html discordIcon} Discord
								</div>
							</button>
						</a>
					</div>
				</div>
			{/snippet}
		</AppBar>
	</header>

	<div class="grid grid-cols-1 md:grid-cols-[auto_1fr]">
		<aside class="hidden md:block">
			<div>
				{#await data.appCats then myCatData}
					<SideBar {myCatData} />
				{/await}
			</div>
		</aside>

		<main>
			{@render children?.()}
		</main>
	</div>

	<footer class="sticky bottom-0 z-10 bg-surface-50-950">
		<div class="md:hidden p-2">
			{#if $page.url.pathname.startsWith('/collections') || $page.url.pathname.startsWith('/rankings') || $page.url.pathname.startsWith('/companies')}
				{#await data.appCats then myCatData}
					<OpenSideBarDrawer {myCatData} />
				{/await}
			{/if}
		</div>
		<div class="inline-flex md:hidden">
			<NavTabs />
		</div>
	</footer>
</div>
