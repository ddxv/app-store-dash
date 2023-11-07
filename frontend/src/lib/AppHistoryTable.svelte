<script lang="ts">
	import type { AppHistoryInfo } from '../types';

	export let history_table: AppHistoryInfo[];
	export let os: string = 'google';
	if (os.includes('google')) {
		os = 'google';
	} else if (os.includes('apple')) {
		os = 'apple';
	}
</script>

<div class="card variant-glass-surface mt-2 md:mt-4 md:p-4">
	<h4 class="h4 md:h3 p-2 mt-2">Recent Raw Data</h4>
	<div class="overflow-x-auto pl-0">
		<table class="table md:table-hover table-compact pl-0">
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
				{#each Object.entries(history_table) as [_prop, values]}
					<tr>
						<td class="!pl-1 !pr-0">
							{values.crawled_date}
						</td>
						{#if os == 'google'}
							<td class="table-cell-fit !px-0">
								{values.installs}
							</td>
						{/if}
						<td class="table-cell-fit !px-0">
							{#if values.rating}
								{values.rating.toFixed(2)}
							{:else}
								null
							{/if}
						</td>
						<td class="table-cell-fit !px-0">
							{values.rating_count}
						</td>
						<td class="table-cell-fit !px-0">
							{values.review_count}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
