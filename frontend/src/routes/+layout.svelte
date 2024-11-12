<script lang="ts">
	import '../app.css';

	import IconSearch from '$lib/svg/IconSearch.svelte';

	import { AppBar } from '@skeletonlabs/skeleton-svelte';

	import type { AfterNavigate } from '@sveltejs/kit';
	import { afterNavigate } from '$app/navigation';

	import githubIcon from '$lib/svg/github-mark.svg?raw';
	import discordIcon from '$lib/svg/discord-mark-black.svg?raw';

	let searchTerm: string = $state();

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
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();

	// Scroll to top after navigation
	afterNavigate((params: AfterNavigate) => {
		const isNewPage: boolean = params.from?.route.id !== params.to?.route.id;
		const elemPage = document.querySelector('#page');
		if (isNewPage && elemPage !== null) {
			elemPage.scrollTop = 0;
		}
	});
</script>

<div class="h-screen grid grid-rows-[auto_1fr_auto]">
	<header class="sticky top-0 z-10">
		<div class="grid-cols-[1fr_0_1fr] md:grid-cols-[0.4fr_1fr_0.3fr]">
			<AppBar
				headlineClasses="sm:hidden"
				centerClasses="hidden sm:block"
				background="bg-tonal-primary"
			>
				{#snippet lead()}
					<div class="flex items-center">
						<a class="flex" href="/">
							<img
								class="ml-1 md:ml-2 h-8 m w-8 md:h-12 md:w-12"
								src="/goblin_purple_hat_250.png"
								alt="Goblin Icon"
							/>
							<strong class="text-xl ml-1 md:ml-2 md:text-3xl uppercase text-primary-900-100"
								>AppGoblin</strong
							>
						</a>
					</div>
				{/snippet}

				<div class="hidden lg:inline-flex">
					<NavTabs />
				</div>

				{#snippet trail()}
					<div>
						<div class="input-group grid-cols-2 sm:grid-cols-[50px_auto]">
							<div class="input-group-shim p-0 md:p-3">
								<IconSearch />
							</div>
							<input
								type="search"
								bind:value={searchTerm}
								onkeydown={navigateToSearch}
								placeholder="Search"
								class="p-0 md:p-3"
							/>
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
		</div>
	</header>

	<main class="bg-surface-100-900">
		{@render children?.()}
	</main>

	<footer class="bg-blue-500 p-4">
		{#snippet footer()}
			{#snippet lead()}
				<div class="inline-flex">
					<NavTabs />
				</div>
			{/snippet}
		{/snippet}
	</footer>
</div>
