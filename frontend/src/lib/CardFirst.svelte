<script lang="ts">
	interface Props {
		header?: import('svelte').Snippet;
		footer?: import('svelte').Snippet;
		children: import('svelte').Snippet;
	}
	let { header, footer, children }: Props = $props();
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
