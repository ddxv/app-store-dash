<script lang="ts">
	import { page } from '$app/stores';
	let { myTabs } = $props();

	function typeTabClass(tab: string) {
		const selectedClass =
			'px-4 py-2 border-2 border-b-0 border-primary-100-900 preset-tonal rounded-t-md relative top-[1px]';
		const unselectedClass =
			'px-4 py-2 border-b-2 border-transparent border-surface-100-900 hover:border-primary-300 hover:';
		if (tab === 'all') {
			return $page.url.pathname === '/companies' ? selectedClass : unselectedClass;
		} else if ($page.url.pathname.startsWith(`/companies/types/${tab}`)) {
			return selectedClass;
		} else return unselectedClass;
	}
</script>

<div class="flex flex-row border-b border-gray-200 bg-gray-50">
	<a href="/companies" class={typeTabClass('all')}>All</a>
	{#each myTabs.types as tab}
		<a href="/companies/types/{tab.url_slug}" class={typeTabClass(tab.url_slug)}>{tab.name}</a>
	{/each}
</div>
