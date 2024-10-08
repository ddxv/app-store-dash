<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler } from '@vincjo/datatables/remote';
	import type { State } from '@vincjo/datatables/remote';
	import type { CompaniesOverviewEntries } from '../types';

	export let entries_table: CompaniesOverviewEntries[];

	const totalRows = entries_table.length;

	const rowsPerPage = 100;

	const handler = new DataHandler<CompaniesOverviewEntries>([], {
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
	console.log(`TABLE ${totalRows}`);
</script>

<div class="table-container space-y-4">
	<div class="overflow-x-auto pl-0">
		<table class="table table-hover table-compact table-auto w-full">
			<thead>
				<tr>
					<th class="table-cell-fit">Ad Domain</th>
					<th class="table-cell-fit">Publisher ID</th>
					<th class="table-cell-fit">Crawled At</th>
					<th class="table-cell-fit">Crawled At</th>
				</tr>
			</thead>
			<tbody>
				{#each $rows as row}
					<tr>
						<td class="table-cell-fit">
							{row.ad_network}
						</td>
						<td class="table-cell-fit">
							{row.store}
						</td>
						<td class="table-cell-fit">
							{row.tag_source}
						</td>
						<td class="table-cell-fit">
							{row.app_count}
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
