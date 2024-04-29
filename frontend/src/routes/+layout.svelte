<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import IconSearch from '$lib/svg/IconSearch.svelte';
	import type { AfterNavigate } from '@sveltejs/kit';
	import { afterNavigate } from '$app/navigation';

	import githubIcon from '$lib/svg/github-mark.svg?raw';

	let searchTerm: string;

	function navigateToSearch(event: any) {
		if (event.key === 'Enter' && searchTerm.trim() !== '') {
			// Replace spaces with '+'
			const encodedSearchTerm = encodeURIComponent(searchTerm.replace(/\s+/g, '+'));

			// Navigate to the search route
			window.location.href = `/search/${encodedSearchTerm}`;
		}
	}

	import NavTabs from '$lib/NavTabs.svelte';

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
						<strong class="text-2xl ml-4 md:text-3xl uppercase">AppGoblin</strong>
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
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://github.com/OpenAttribution/open-attribution"
					target="_blank"
					rel="noreferrer"
				>
					<div class="inline-flex items-center">
						{@html githubIcon}
						<h6 class="h6 p-2 justify-center text-center">Open Source on GitHub</h6>
					</div>
				</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="footer">
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
		</AppBar>
	</svelte:fragment>

	<slot />

	<!-- Page Route Content -->
</AppShell>
