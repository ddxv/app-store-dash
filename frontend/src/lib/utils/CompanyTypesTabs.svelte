<script lang="ts">
	import { page } from '$app/stores';
	let { myTabs } = $props();

	function typeTabClass(tab: string) {
		const selectedClass =
			'px-2 md:px-4 py-2 border-t-2 border-r-2 border-l-2 border-primary-100-900 rounded-t-md relative top-[1px]';
		const unselectedClass =
			'px-2 md:px-4 py-2 border-b-2 border-surface-800-200 hover:border-primary-300-700 hover:border-b-2 hover:underline';
		if (tab === 'all') {
			return $page.url.pathname === '/companies' ? selectedClass : unselectedClass;
		} else if ($page.url.pathname.startsWith(`/companies/types/${tab}`)) {
			return selectedClass;
		} else return unselectedClass;
	}
</script>

<div class="flex flex-row flex-wrap text-sm md:text-base">
	<a href="/companies" class={typeTabClass('all')}>All</a>
	{#each myTabs.types as tab}
		<a href="/companies/types/{tab.url_slug}" class={typeTabClass(tab.url_slug)}>{tab.name}</a>
	{/each}
</div>
