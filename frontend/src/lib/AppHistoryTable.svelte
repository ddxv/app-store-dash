<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler } from '@vincjo/datatables/remote';
	import type { State } from '@vincjo/datatables/remote';
	import type { AppHistoryInfo } from '../types';

	export let history_table: AppHistoryInfo[];

	const totalRows = history_table.length;
	const rowsPerPage = 10;

	const handler = new DataHandler<AppHistoryInfo>([], {
		rowsPerPage: rowsPerPage,
		totalRows: totalRows
	});
	const rows = handler.getRows();

	handler.onChange(
		(state: State) =>
			Promise.resolve(
				history_table.slice(
					0 + (state.pageNumber - 1) * state.rowsPerPage,
					state.rowsPerPage * state.pageNumber
				)
			)
		// Promise.resolve(history_table.slice(0 + state.offset, 20 + state.offset))
	);

	handler.invalidate();

	export let os: string = 'google';
	if (os.includes('google')) {
		os = 'google';
	} else if (os.includes('apple')) {
		os = 'apple';
	}

	const numberFormatter = new Intl.NumberFormat('en-US');
</script>

<div class="table-container space-y-4">
	<div class="card variant-glass-surface mt-2 md:mt-4 md:p-4">
		<h4 class="h4 md:h3 p-2 mt-2">Recent Raw Data</h4>
		<div class="overflow-x-auto pl-0">
			<!-- <table class="table md:table-hover table-compact"> -->
			<table class="table table-hover table-compact table-auto w-full">
				<thead>
					<tr>
						<th class="table-cell-fit !pl-1 !pr-0">Date</th>
						{#if os == 'google'}
							<th class="table-cell-fit !px-0">Installs</th>
						{/if}
						<th class="table-cell-fit !px-0">Rating</th>
						<th class="table-cell-fit !px-0">Ratings</th>
						<th class="table-cell-fit !px-0">Reviews</th>
					</tr>
				</thead>
				<tbody>
					<!-- {#each Object.entries(history_table) as [_prop, values]} -->
					{#each $rows as row}
						<tr>
							<td class="!pl-1 !pr-0">
								{row.crawled_date}
							</td>
							{#if os == 'google'}
								<td class="table-cell-fit !px-0">
									{numberFormatter.format(row.installs)}
								</td>
							{/if}
							<td class="table-cell-fit !px-0">
								{#if row.rating}
									{row.rating.toFixed(2)}
								{:else}
									null
								{/if}
							</td>
							<td class="table-cell-fit !px-0">
								{numberFormatter.format(row.rating_count)}
							</td>
							<td class="table-cell-fit !px-0">
								{numberFormatter.format(row.review_count)}
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
</div>
