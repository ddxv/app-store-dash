<!-- @migration-task Error while migrating Svelte code: `<a>` is invalid inside `<tr>` -->
<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler } from '@vincjo/datatables/legacy/remote';
	import type { State } from '@vincjo/datatables/legacy/remote';
	import type { CompanyOverviewApps } from '../types';

	export let entries_table: CompanyOverviewApps[];

	const totalRows = entries_table.length;

	const rowsPerPage = 100;

	const handler = new DataHandler<CompanyOverviewApps>([], {
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
	console.log(`TABLE Company: ${totalRows}`);

	$: firstRowInstalls =
		entries_table &&
		entries_table.length > 0 &&
		typeof entries_table[0].installs === 'string' &&
		entries_table[0].installs != 'N/A';
</script>

<div class="table-container space-y-4">
	<div class="overflow-x-auto pl-0">
		<table class="table table-hover table-compact table-auto w-full">
			<thead>
				<tr>
					<th class="table-cell-fit"></th>
					<th class="table-cell-fit">App</th>
					<th class="table-cell-fit">
						{#if firstRowInstalls}
							Installs
						{:else}
							Ratings
						{/if}
					</th>
				</tr>
			</thead>
			<tbody>
				{#each $rows as row, index}
					<tr style="cursor: pointer;" class="px-0">
						<td class="table-cell-fit">
							{index + 1}
						</td>
						<td class="table-cell-fit">
							<!-- TODO: This is supposed to be just inside TR for whole row -->
							<a href="/apps/{row.store_id}" class="table-row-link">
								{row.name}
							</a>
						</td>

						<td class="table-cell-fit">
							{#if row.installs && typeof row.installs === 'string' && row.installs != 'N/A'}
								{row.installs}
							{:else}
								{row.rating_count}
							{/if}
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

<style>
	.table-row-link {
		display: contents;
		text-decoration: none;
		color: inherit;
	}
	.table-row-link:hover td {
		background-color: #f5f5f5;
	}
</style>
