<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler, RowsPerPage } from '@vincjo/datatables/remote';
	import type { State } from '@vincjo/datatables/remote';
	import type { AdsTxtEntries } from '../types';

	export let entries_table: AdsTxtEntries[];

	const totalRows = entries_table.length;

	const rowsPerPage = 10;

	const handler = new DataHandler<AdsTxtEntries>([], {
		rowsPerPage: rowsPerPage,
		totalRows: totalRows
	});
	const rows = handler.getRows();

	handler.onChange((state: State) =>
		Promise.resolve(
			entries_table.slice(
				0 + (state.pageNumber - 1) * state.rowsPerPage,
				state.rowsPerPage * state.pageNumber
			)
		)
	);

	handler.invalidate();
</script>

<div class="table-container space-y-4">
	<div class="overflow-x-auto pl-0">
		<table class="table table-hover table-compact table-auto w-full">
			<thead>
				<tr>
					<th class="table-cell-fit">Ad Domain</th>
					<th class="table-cell-fit">Publisher ID</th>
					<th class="table-cell-fit">Crawled At</th>
				</tr>
			</thead>
			<tbody>
				{#each $rows as row}
					<tr>
						<td class="table-cell-fit">
							{row.ad_domain_url}
						</td>
						<td class="table-cell-fit">
							{row.publisher_id}
						</td>
						<td class="table-cell-fit">
							{new Date(row.developer_domain_crawled_at).toLocaleDateString('en-CA')}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<footer class="flex justify-between">
			<!-- <RowCount {handler} /> -->
			{#if totalRows > rowsPerPage}
				<Pagination {handler} />
			{/if}
		</footer>
	</div>
</div>
