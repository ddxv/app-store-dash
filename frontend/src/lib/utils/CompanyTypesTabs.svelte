<script lang='ts'>
    import { TabGroup, TabAnchor } from "@skeletonlabs/skeleton";
    import { page } from "$app/stores";
    export let myTabs;
</script>

<TabGroup>
	<TabAnchor href="/companies" selected={$page.url.pathname === '/companies'}>All</TabAnchor>
    {#each myTabs as tab}
	<TabAnchor href='/companies/types/{tab.url_slug}' selected={$page.url.pathname === `/companies/types/${tab.url_slug}`}>{tab.name}</TabAnchor>
    {/each}
</TabGroup>

