<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import IconSearch from '$lib/svg/IconSearch.svelte';
	import type { AfterNavigate } from '@sveltejs/kit';
	import { afterNavigate } from '$app/navigation';

	import githubIcon from '$lib/svg/github-mark.svg?raw';
	import discordIcon from '$lib/svg/discord-mark-black.svg?raw';

	let searchTerm: string = $state();

	const bgBarColor = 'from-purple-500/40 via-white to-white';

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

<!-- App Shell -->
<AppShell
	regionPage="p-2 md:p-8"
	slotSidebarLeft="w-0 lg:w-auto"
	slotPageHeader="hidden lg:inline-flex"
>
	{#snippet header()}
		<!-- App Bar -->
		<AppBar
			gridColumns="grid-cols-[1fr_0_1fr] md:grid-cols-[0.4fr_1fr_0.3fr]"
			slotLead="p-2"
			slotTrail="p-2"
			spacing="space-y-0"
			padding="p-0"
			class="bg-gradient-to-br {bgBarColor}"
		>
			{#snippet lead()}
				<div class="flex items-center">
					<a class="flex" href="/">
						<!-- <img class="h-8 m w-8 md:h-12 md:w-12" src="/cute_eyes_250.png" alt="Goblin Icon" /> -->
						<img
							class="ml-2 h-8 m w-8 md:h-12 md:w-12"
							src="/goblin_purple_hat_250.png"
							alt="Goblin Icon"
						/>
						<strong class="text-xl ml-2 md:text-3xl uppercase">AppGoblin</strong>
					</a>
				</div>
			{/snippet}

			<div class="hidden lg:inline-flex">
				<NavTabs />
			</div>

			{#snippet trail()}
				<div class="input-group grid-cols-2 sm:grid-cols-[50px_auto]">
					<div class="input-group-shim p-1 md:p-3">
						<IconSearch />
					</div>
					<input
						type="search"
						bind:value={searchTerm}
						onkeydown={navigateToSearch}
						placeholder="Search"
						class="p-1 md:p-3"
					/>
				</div>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://github.com/ddxv/app-store-dash"
					target="_blank"
					rel="noreferrer"
				>
					<div class="inline-flex items-center">
						{@html githubIcon} GitHub
					</div>
				</a>
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://discord.gg/7jpWEhkXRW"
					target="_blank"
					rel="noreferrer"
				>
					<div class="inline-flex items-center">
						{@html discordIcon} Discord
					</div>
				</a>
			{/snippet}
		</AppBar>
	{/snippet}
	{#snippet footer()}
		<AppBar
			slotLead="p-0"
			slotTrail="p-2"
			spacing="space-y-0"
			padding="p-0"
			gap="gap-0"
			class="bg-gradient-to-tl {bgBarColor} lg:hidden"
			gridColumns="grid-cols-[auto_1fr_auto]"
		>
			{#snippet lead()}
				<div class="inline-flex">
					<NavTabs />
				</div>
			{/snippet}
		</AppBar>
	{/snippet}

	{@render children?.()}

	<!-- Page Route Content -->
</AppShell>
