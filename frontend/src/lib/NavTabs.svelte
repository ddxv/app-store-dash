<script lang="ts">
	import { page } from '$app/stores';
	import { TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
	const topBarFont = 'h6 md:h3';
</script>

<TabGroup
	active="variant-filled-primary"
	hover="hover:variant-soft-primary"
	flex="flex-1"
	rounded=""
	border=""
	class="w-full p-0"
	padding="px-1 py-4 md:px-4"
>
	<TabAnchor class="p-0 px-0" href="/" selected={$page.url.pathname == '/'}>
		<h3 class={topBarFont}>HOME</h3>
	</TabAnchor>
	<TabAnchor
		href="/collections/new_monthly"
		selected={$page.url.pathname.startsWith('/collections')}
	>
		<h3 class={topBarFont}>NEW</h3>
	</TabAnchor>
	<TabAnchor
		href="/rankings/store/1/collection/1/category/1"
		selected={$page.url.pathname.startsWith('/rankings')}
	>
		<h3 class={topBarFont}>RANKS</h3>
	</TabAnchor>
	<TabAnchor
		href="/adtech/Google/networks?groupby=brands&metric=appcount"
		selected={$page.url.pathname.startsWith('/adtech')}
		><h3 class={topBarFont}>ADTECH</h3></TabAnchor
	>
	<TabAnchor href="/about" selected={$page.url.pathname === '/about'}
		><h3 class={topBarFont}>ABOUT</h3></TabAnchor
	>
</TabGroup>
