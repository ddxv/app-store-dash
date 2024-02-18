<script lang="ts">
	import { page } from '$app/stores';
	import { TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
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
		<h3 class="h5 md:h3">HOME</h3>
	</TabAnchor>
	<TabAnchor
		href="/collections/new_monthly"
		selected={$page.url.pathname.startsWith('/collections')}
	>
		<h3 class="h5 md:h3">NEW</h3>
	</TabAnchor>
	<TabAnchor
		href="/rankings/store/1/collection/1/category/1"
		selected={$page.url.pathname.startsWith('/rankings')}
	>
		<h3 class="h5 md:h3">RANKS</h3>
	</TabAnchor>
	<TabAnchor href="/adtech" selected={$page.url.pathname.startsWith('/adtech')}
		><h3 class="h5 md:h3">ADTECH</h3></TabAnchor
	>
	<TabAnchor href="/about" selected={$page.url.pathname === '/about'}
		><h3 class="h5 md:h3">ABOUT</h3></TabAnchor
	>
</TabGroup>
