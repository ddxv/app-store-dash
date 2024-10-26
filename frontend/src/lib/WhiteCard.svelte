<script>
	/**
	 * @typedef {Object} Props
	 * @property {import('svelte').Snippet} [title]
	 * @property {import('svelte').Snippet} [children]
	 */

	/** @type {Props} */
	let { title, children } = $props();
</script>

<div class="card bg-white rounded-lg overflow-hidden">
	{#if title}
		<div class="card-header text-2xl bg-surface-50 border-b border-gray-200">
			{@render title?.()}
		</div>
	{/if}
	<div class="card-content">
		{@render children?.()}
	</div>
</div>
