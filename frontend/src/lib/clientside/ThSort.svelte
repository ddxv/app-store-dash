<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables';

	interface Props {
		handler: DataHandler;
		orderBy: string;
		children?: import('svelte').Snippet;
	}

	let { handler, orderBy, children }: Props = $props();

	const sorted = handler.getSort();
</script>

<th onclick={() => handler.sort(orderBy)} class="cursor-pointer select-none">
	<div class="flex h-full items-center justify-start gap-x-2">
		{@render children?.()}
		{#if $sorted.identifier === orderBy}
			{#if $sorted.direction === 'asc'}
				&darr;
			{:else if $sorted.direction === 'desc'}
				&uarr;
			{/if}
		{:else}
			&updownarrow;
		{/if}
	</div>
</th>
