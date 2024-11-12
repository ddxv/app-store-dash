<script>
	let { header, footer, children } = $props();
</script>

<div class="card p-2 preset-tonal">
	{#if header}
		<header>
			{@render header()}
			<hr class="mb-2 border-surface-100-900" />
		</header>
	{/if}

	{@render children?.()}

	{#if footer}
		<footer>
			{@render footer?.()}
		</footer>
	{/if}
</div>
