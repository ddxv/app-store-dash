<script lang="ts">
	import Pagination from './Pagination.svelte';

	import { DataHandler } from '@vincjo/datatables/legacy/remote';
	import type { State } from '@vincjo/datatables/legacy/remote';

	import IconiOs from './svg/IconiOS.svelte';
	import IconGoogle from './svg/IconGoogle.svelte';

	import { page } from '$app/stores';

	let pattern = $page.params.pattern;

	import type { SdkOverview } from '../types';

	let { entries_table, is_ios }: { entries_table: SdkOverview[]; is_ios: boolean } = $props();

	const totalRows = entries_table.length;

	const rowsPerPage = 100;

	const handler = new DataHandler<SdkOverview>([], {
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
	console.log(`TABLE sdks: ${totalRows}`);

	function formatNumber(num: number) {
		if (num >= 1000000000000) return (num / 1000000000000).toFixed(1).replace(/\.0$/, '') + 'T';
		if (num >= 1000000000) return (num / 1000000000).toFixed(1).replace(/\.0$/, '') + 'B';
		if (num >= 1000000) return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
		if (num >= 1000) return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'K';
		return num;
	}
</script>

<div class="table-container space-y-4 p-2 md:p-4">
	<div class="overflow-x-auto pl-0 max-w-full">
		<table class="md:table table-hover table-compact w-full text-xs">
			<thead>
				<tr>
					<th class="truncate">Value Name</th>
					<th class="table-cell-fit">App</th>
					{#if !is_ios}
						<th class="table-cell-fit">Installs</th>
					{/if}
					<th class="table-cell-fit">Rating Count</th>
				</tr>
			</thead>
			<tbody>
				{#each $rows as row}
					<tr class="px-0">
						<td class="truncate">
							{#if row.value_name != pattern}
								<a href={`/sdks/${row.value_name}`}>
									{row.value_name}
								</a>
							{:else}
								full match
							{/if}
						</td>

						<td class="table-cell-fit">
							<a href={`/apps/${row.store_id}`} class="inline-flex gap-1 md:gap-2">
								<div>
									{#if row.store.startsWith('Google')}
										<IconGoogle size={16} />
									{:else}
										<IconiOs size={16} />
									{/if}
								</div>
								{row.app_name}
							</a>
						</td>
						{#if !is_ios}
							<td class="table-cell-fit">
								{formatNumber(row.installs)}
							</td>
						{/if}
						<td class="table-cell-fit">
							{formatNumber(row.rating_count)}
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
