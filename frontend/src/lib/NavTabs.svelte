<script lang="ts">
	const topBarFont = 'text-base md:h4 hover:text-surface-500';
	const horizontalDivider = 'h-12 w-px bg-primary-900-100';
	const topDivider = 'md:hidden border-t-[1px] border-primary-900-100 p-2';
</script>

<div class={topDivider}></div>
<div class="flex flex-row gap-2 md:gap-6 text-center items-center">
	<a href="/collections/new_monthly">
		<p class={topBarFont}>NEW APPS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/rankings/store/1/collection/1/category/1" class={topBarFont}>
		<p class={topBarFont}>APP RANKS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/adtech/Google/networks?groupby=brands&metric=appcount" class={topBarFont}>
		<p class={topBarFont}>ADTECH RANKS</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/companies" class={topBarFont}>
		<p class={topBarFont}>COMPANIES</p>
	</a>
	<div class={horizontalDivider}></div>
	<a href="/about" class={topBarFont}>
		<p class={topBarFont}>ABOUT</p>
	</a>
</div>
