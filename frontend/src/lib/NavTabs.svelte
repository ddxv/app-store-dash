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
>
	<TabAnchor class="p-0 px-0" href="/" selected={$page.url.pathname == '/'}>
		<h3 class="h4 md:h3 md:p-2">HOME</h3>
	</TabAnchor>
	<TabAnchor
		class="p-0 px-0"
		href="/collections/new_monthly"
		selected={$page.url.pathname.startsWith('/collections')}
	>
		<h3 class="h4 md:h3 md:p-2">NEW</h3>
	</TabAnchor>
	<TabAnchor
		href="/rankings/store/1/collection/1/category/1"
		selected={$page.url.pathname.startsWith('/rankings')}
	>
		<h3 class="h4 md:h3 md:p-2">RANKS</h3>
	</TabAnchor>
	<TabAnchor href="/trackers" selected={$page.url.pathname === '/trackers'}
		><h3 class="h4 md:h3 md:p-2">TRACKERS</h3></TabAnchor
	>
	<TabAnchor href="/networks" selected={$page.url.pathname === '/networks'}
		><h3 class="h4 md:h3 md:p-2">NETWORKS</h3></TabAnchor
	>
	<TabAnchor href="/about" selected={$page.url.pathname === '/about'}
		><h3 class="h4 md:h3 md:p-2">ABOUT</h3></TabAnchor
	>
</TabGroup>
