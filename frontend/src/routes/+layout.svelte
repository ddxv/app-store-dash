<script>
	import '../app.postcss';
	import { AppShell, AppBar, TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import SearchIcon from '../../static/SearchIcon.svelte';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	export let valueSingle = 'books';
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<!-- App Shell -->
<AppShell regionPage="p-8">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-xl uppercase">App Store Data</strong>
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
				<TabAnchor href="/categories" selected={$page.url.pathname === '/categories'}>
					<span>CATEGORIES</span>
				</TabAnchor>
				<TabAnchor href="/about" selected={$page.url.pathname === '/about'}>
					<span>ABOUT</span>
				</TabAnchor>
			</TabGroup>
			<svelte:fragment slot="trail">
				<div class="input-group grid-cols-[auto_1fr_auto]">
					<div class="input-group-shim">
						<SearchIcon />
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
				<ListBox>
					<br />
					Type
					<hr class="!border-t-2" />
					<ListBoxItem bind:group={valueSingle} name="medium" value="google">Google</ListBoxItem>
					<ListBoxItem bind:group={valueSingle} name="medium" value="ios">iOS</ListBoxItem>
					<br />
					Categories
					<hr class="!border-t-2" />
					<ListBoxItem bind:group={valueSingle} name="medium" value="books">BOOKS</ListBoxItem>
					<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
					{#if data}
						{#each Object.entries(data.mycats.categories) as [_prop, values]}
							<ListBoxItem bind:group={valueSingle} name="medium" value="${values.id}"
								>{values.name}</ListBoxItem
							>
						{/each}
					{/if}
				</ListBox>
			</div>
		{/if}
		<!-- --- -->
	</svelte:fragment>
	<slot />
	<!-- Page Route Content -->
</AppShell>
