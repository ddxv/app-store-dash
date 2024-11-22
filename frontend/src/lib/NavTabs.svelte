<script lang="ts">
	import { page } from '$app/stores';
	const topBarFont = 'text-base hover:text-primary-900-100';
	const topBarHighlightedFont = 'text-base text-primary-900-100';
	const horizontalDivider = 'h-12 w-px bg-secondary-100-900';
	const topDivider =
		'w-full border-t-[1px] md:border-t-0 md:border-b-[1px] border-secondary-100-900 p-2';
	function isHighlighted(path: string) {
		return $page.url.pathname.startsWith(path);
	}
</script>

<div class="flex flex-row gap-2 md:gap-6 text-center items-center {topDivider} mx-2">
	<a href="/companies" class={topBarFont}>
		<p class={isHighlighted('/companies') ? topBarHighlightedFont : topBarFont}>COMPANY RANKS</p>
	</a>

	<div class={horizontalDivider}></div>
	<a href="/rankings/store/1/collection/1/category/1" class={topBarFont}>
		<p class={isHighlighted('/rankings') ? topBarHighlightedFont : topBarFont}>APP RANKS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/sdks" class={topBarFont}>
		<p class={isHighlighted('/sdks') ? topBarHighlightedFont : topBarFont}>APP SDK</p>
	</a>

	<div class={horizontalDivider}></div>
	<a href="/collections/new_monthly">
		<p class={isHighlighted('/collections') ? topBarHighlightedFont : topBarFont}>NEW APPS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/about" class={topBarFont}>
		<p class={isHighlighted('/about') ? topBarHighlightedFont : topBarFont}>ABOUT</p>
	</a>
</div>
