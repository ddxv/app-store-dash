<script>
	/**
	 * @typedef {Object} Props
	 * @property {import('svelte').Snippet} [card1]
	 * @property {import('svelte').Snippet} [card2]
	 * @property {import('svelte').Snippet} [card3]
	 * @property {import('svelte').Snippet} [card4]
	 */

	/** @type {Props} */
	let { card1, card2, card3, card4 } = $props();
</script>

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	{@render card1?.()}
	{@render card2?.()}
	{#if card3}
		<!-- This is always true? -->
		{@render card3?.()}
		<div class="col-span-3">
			{@render card4?.()}
		</div>
	{:else}
		{@render card4?.()}
	{/if}
</div>
