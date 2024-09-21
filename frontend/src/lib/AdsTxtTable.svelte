<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler } from '@vincjo/datatables/remote';
	import type { State } from '@vincjo/datatables/remote';
	import type { AdsTxtEntries } from '../types';

	export let entries_table: AdsTxtEntries[];

	const totalRows = entries_table.length;

	const handler = new DataHandler<AdsTxtEntries>([], { rowsPerPage: 10, totalRows: totalRows });
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
	<div class="card variant-glass-surface mt-2 md:mt-4 md:p-4">
		<h4 class="h4 md:h3 p-2 mt-2">App Ads-Txt Entries</h4>
		<div class="overflow-x-auto pl-0">
			<table class="table table-hover table-compact table-auto w-full">
				<thead>
					<tr>
						<th class="table-cell-fit !pl-1 !pr-0">Ad Domain</th>
						<th class="table-cell-fit !px-0">Ad Domain URL</th>
						<th class="table-cell-fit !px-0">Publisher ID</th>
						<th class="table-cell-fit !px-0">Relationship</th>
						<th class="table-cell-fit !px-0">crawl_result</th>
						<th class="table-cell-fit !px-0">Developer Domain Crawled At</th>
					</tr>
				</thead>
				<tbody>
					{#each $rows as row}
						<tr>
							<td class="!pl-1 !pr-0">
								{row.ad_domain}
							</td>
							<td class="table-cell-fit !px-0">
								{row.ad_domain_url}
							</td>
							<td class="table-cell-fit !px-0">
								{row.publisher_id}
							</td>
							<td class="table-cell-fit !px-0">
								{row.relationship}
							</td>
							<td class="table-cell-fit !px-0">
								{row.crawl_result}
							</td>
							<td class="table-cell-fit !px-0">
								{row.developer_domain_crawled_at}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
			<footer class="flex justify-between">
				<!-- <RowCount {handler} /> -->
				<Pagination {handler} />
			</footer>
		</div>
	</div>
</div>
