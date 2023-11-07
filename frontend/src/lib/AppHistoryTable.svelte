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
	<div class="table-container overflow-x-auto">
		<table class="table table-hover table-auto">
			<thead>
				<tr>
					<th>Date</th>
					{#if os == 'google'}
						<th>Installs</th>
					{/if}
					<th>Rating</th>
					<th>Ratings</th>
					<th>Reviews</th>
				</tr>
			</thead>
			<tbody>
				{#each Object.entries(history_table) as [_prop, values]}
					<tr>
						<td>
							{values.crawled_date}
						</td>
						{#if os == 'google'}
							<td>
								{values.installs}
							</td>
						{/if}
						<td>
							{#if values.rating}
								{values.rating.toFixed(2)}
							{:else}
								null
							{/if}
						</td>
						<td>
							{values.rating_count}
						</td>
						<td>
							{values.review_count}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
