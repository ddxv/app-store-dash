<script lang="ts">
	import Pagination from './Pagination.svelte';

	// import { DataHandler } from '@vincjo/datatables/remote';
	import { DataHandler } from '@vincjo/datatables';
	// import type { State } from '@vincjo/datatables/remote';
	import type { CompaniesOverviewEntries } from '../types';

	import ThSort from './clientside/ThSort.svelte';

	export let entries_table: CompaniesOverviewEntries[];

	const totalRows = entries_table.length;

	const rowsPerPage = 100;

	const handler = new DataHandler<CompaniesOverviewEntries>(entries_table, {
		rowsPerPage: rowsPerPage,
		// totalRows: totalRows
	});

	const rows = handler.getRows();

	// handler.onChange((state: State) =>
	// 	Promise.resolve(
	// 		entries_table.slice(
	// 			0 + (state.pageNumber - 1) * state.rowsPerPage,
	// 			state.rowsPerPage * state.pageNumber
	// 		)
	// 	)
	// );

	// handler.invalidate();
	console.log(`TABLE Companies: ${totalRows}`);
</script>

<div class="table-container space-y-4">
	<div class="overflow-x-auto pl-0">
		<table class="table table-hover table-compact table-auto w-full">
			<thead>
				<tr>
					<th class="table-cell-fit"></th>
				<ThSort {handler} orderBy="company_name">Company</ThSort>
                <ThSort {handler} orderBy="percentage">Apps</ThSort>
					<!-- <th class="table-cell-fit">Company</th> -->
					<!-- <th class="table-cell-fit">Apps</th> -->
				</tr>
			</thead>
			<tbody>
				{#each $rows as row, index}
					<tr style="cursor: pointer;" class="px-0">
						<a href="/companies/{row.company_domain}" class="table-row-link">
							<td class="table-cell-fit">
								{index + 1}
							</td>
							{#if row.company_name}
								<td class="table-cell-fit">
									{row.company_name}
									({row.company_domain})
								</td>
							{:else}
								<td class="table-cell-fit">
									{row.company_domain}
								</td>
							{/if}
							<td class="table-cell-fit">
								{(row.percentage * 100).toFixed(2)}%
							</td>
						</a></tr
					>
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
