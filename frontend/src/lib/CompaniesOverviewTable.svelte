<script lang="ts">
	import Pagination from './Pagination.svelte';
	import { DataHandler } from '@vincjo/datatables';
	import type { CompaniesOverviewEntries } from '../types';
	import ThSort from './clientside/ThSort.svelte';
	// import ThFilter from './clientside/ThFilter.svelte';

	import { page } from "$app/stores";

	export let entries_table: CompaniesOverviewEntries[];

	const totalRows = entries_table.length;

	const rowsPerPage = 100;

	const handler = new DataHandler<CompaniesOverviewEntries>(entries_table, {
		rowsPerPage: rowsPerPage,
	});

	const rows = handler.getRows();

	console.log(`TABLE Companies: ${totalRows}`);
</script>

<div class="table-container space-y-4">
	<div class="overflow-x-auto pl-0">
		<table class="table table-hover table-compact table-auto w-full">
			<thead>
				<tr>
					<th class="table-cell-fit"></th>
					<ThSort {handler} orderBy="company_name">Company</ThSort>
                	<ThSort {handler} orderBy="google_sdk">Android SDK</ThSort>
                	<ThSort {handler} orderBy="apple_sdk">iOS SDK</ThSort>
					{#if ( !$page.params.type || $page.params.type == 'ad-networks')}
						<ThSort {handler} orderBy="google_app_ads_direct">Android AdsTxt</ThSort>
						<ThSort {handler} orderBy="apple_app_ads_direct">iOS AdsTxt</ThSort>
					{/if}
				</tr>
				
			</thead>
			<tbody>
				{#each $rows as row, index}
					<tr style="cursor: pointer;" class="px-0">
						<a href="/companies/{row.company_domain}" class="table-row-link">
							<td class="table-cell-fit">
								{index + 1}
							</td>
								<td class="table-cell-fit">
							{#if row.company_name}
									{row.company_name}
									({row.company_domain})
							{:else}
									{row.company_domain}
							{/if}
								</td>
							<td class="table-cell-fit">
								{(row.google_sdk * 100).toFixed(2)}%
							</td>

							<td class="table-cell-fit">
								{(row.apple_sdk * 100).toFixed(2)}%
							</td>

							{#if ( !$page.params.type || $page.params.type == 'ad-networks')}
								<td class="table-cell-fit">
								{(row.google_app_ads_direct * 100).toFixed(2)}%
							</td>

							<td class="table-cell-fit">
									{(row.apple_app_ads_direct * 100).toFixed(2)}%
								</td>
							{/if}
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
