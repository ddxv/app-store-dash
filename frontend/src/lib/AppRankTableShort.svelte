<script lang="ts">
	import type { RankedAppList } from '../types';

	interface Props {
		myTable: RankedAppList;
	}

	let { myTable }: Props = $props();
</script>

<table class="table table-hover table-compact">
	<thead>
		<!-- <tr>
			<th>Rank</th>
			<th>Name</th>
		</tr> -->
	</thead>
	<tbody>
		{#each Object.entries(myTable.ranks) as [_prop, values]}
			<tr>
				<td
					><div class="inline-flex">
						#
						<h3 class="h4 md:h3">
							{values.rank}
						</h3>
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
