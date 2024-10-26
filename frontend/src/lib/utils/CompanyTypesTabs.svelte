<script lang="ts">
	import { TabGroup, TabAnchor } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	let { myTabs } = $props();
</script>

<TabGroup>
	<TabAnchor href="/companies" selected={$page.url.pathname === '/companies'}>All</TabAnchor>
	{#each myTabs as tab}
		<TabAnchor
			href="/companies/types/{tab.url_slug}"
			selected={$page.url.pathname.startsWith(`/companies/types/${tab.url_slug}`)}
			>{tab.name}</TabAnchor
		>
	{/each}
</TabGroup>
