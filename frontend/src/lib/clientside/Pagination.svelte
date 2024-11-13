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
<section class="btn-group preset-tonal-surface [&>*+*]:border-surface-500 h-10 hidden lg:block">
	<button
		type="button"
		class="hover:preset-tonal-primary"
		class:disabled={$pageNumber === 1}
		onclick={() => handler.setPage('previous')}
	>
		←
	</button>
	{#each $pages as page}
		<button
			type="button"
			class="hover:preset-tonal-primary"
			class:active={$pageNumber === page}
			class:ellipse={page === null}
			onclick={() => handler.setPage(page)}
		>
			{page ?? '...'}
		</button>
	{/each}
	<button
		type="button"
		class="hover:preset-tonal-primary"
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
		class="btn preset-tonal-surface mr-2 mb-2 hover:preset-tonal-primary"
		class:disabled={$pageNumber === 1}
		onclick={() => handler.setPage('previous')}
	>
		←
	</button>
	<button
		type="button"
		class="btn preset-tonal-surface mb-2 hover:preset-tonal-primary"
		class:disabled={$pageNumber === $pageCount}
		onclick={() => handler.setPage('next')}
	>
		→
	</button>
</section>
