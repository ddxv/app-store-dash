<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables/legacy';
	interface Props {
		handler: DataHandler;
	}

	let { handler }: Props = $props();
	const pageNumber = handler.getPageNumber();
	const pageCount = handler.getPageCount();
	const pages = handler.getPages({ ellipsis: true });
</script>

<!-- Desktop buttons -->
<section class="btn-group variant-ghost-surface [&>*+*]:border-surface-500 h-10 hidden lg:block">
	<button
		type="button"
		class="hover:variant-soft-primary"
		class:disabled={$pageNumber === 1}
		onclick={() => handler.setPage('previous')}
	>
		←
	</button>
	{#each $pages as page}
		<button
			type="button"
			class="hover:variant-soft-primary"
			class:active={$pageNumber === page}
			class:ellipse={page === null}
			onclick={() => handler.setPage(page)}
		>
			{page ?? '...'}
		</button>
	{/each}
	<button
		type="button"
		class="hover:variant-soft-primary"
		class:disabled={$pageNumber === $pageCount}
		onclick={() => handler.setPage('next')}
	>
		→
	</button>
</section>

<!-- Mobile buttons -->
<section class="lg:hidden">
	<button
		type="button"
		class="btn variant-ghost-surface mr-2 mb-2 hover:variant-soft-primary"
		class:disabled={$pageNumber === 1}
		onclick={() => handler.setPage('previous')}
	>
		←
	</button>
	<button
		type="button"
		class="btn variant-ghost-surface mb-2 hover:variant-soft-primary"
		class:disabled={$pageNumber === $pageCount}
		onclick={() => handler.setPage('next')}
	>
		→
	</button>
</section>
