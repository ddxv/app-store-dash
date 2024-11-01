<script lang="ts">
	import type { Snippet } from 'svelte';
	let {
		card1,
		card2,
		card3,
		card4
	}: { card1?: Snippet; card2?: Snippet; card3?: Snippet; card4?: Snippet } = $props();
</script>

<div class="flex flex-col gap-4 md:gap-6">
	<div class="md:grid md:grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">
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
