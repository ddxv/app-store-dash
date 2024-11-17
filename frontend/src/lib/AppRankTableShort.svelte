<script lang="ts">
	import type { RankedAppList } from '../types';

	interface Props {
		myTable: RankedAppList;
	}

	let { myTable }: Props = $props();
</script>

<div class="card preset-filled-surface-100-900 rounded-md">
	<table class="table table-hover table-compact">
		<thead> </thead>
		<tbody>
			{#each Object.entries(myTable.ranks) as [_prop, values]}
				<tr>
					<td
						><div class="inline-flex">
							<p class="text-sm md:text-base">#</p>
							<p class="text-xl md:text-xl2">
								{values.rank}
							</p>
						</div>
					</td>
					<td>
						<a href="/apps/{values.store_id}">
							<div class="inline-flex">
								<img
									src={values.icon_url_512}
									alt={values.name}
									width="50 md:100"
									referrerpolicy="no-referrer"
								/>
							</div>
						</a>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
