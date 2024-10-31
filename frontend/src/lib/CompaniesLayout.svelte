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

<div class="flex flex-col gap-4 md:gap-6">
	<div class="grid grid-cols-3 gap-4 md:gap-6">
		{@render card1?.()}
		{@render card2?.()}
		{#if card3}
			{@render card3?.()}
			<div class="col-span-3 flex gap-4">
				{@render card4?.()}
			</div>
		{:else}
			{@render card4?.()}
		{/if}
	</div>
</div>
