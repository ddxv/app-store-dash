<script lang="ts">
	const topBarFont = 'text-base md:h4 hover:text-surface-500';
	const horizontalDivider = 'h-12 w-px bg-secondary-100-900';
	const topDivider =
		'w-full border-t-[1px] md:border-t-0 md:border-b-[1px] border-secondary-100-900 p-2';
</script>

<div class="flex flex-row gap-2 md:gap-6 text-center items-center {topDivider} mx-2">
	<a href="/collections/new_monthly">
		<p class={topBarFont}>NEW APPS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/rankings/store/1/collection/1/category/1" class={topBarFont}>
		<p class={topBarFont}>APP RANKS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/sdks" class={topBarFont}>
		<p class={topBarFont}>APP SDK</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/companies" class={topBarFont}>
		<p class={topBarFont}>COMPANY RANKS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/about" class={topBarFont}>
		<p class={topBarFont}>ABOUT</p>
	</a>
</div>
