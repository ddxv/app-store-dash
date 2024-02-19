<script lang="ts">
	import type { Company } from '../types';
	export let tabledata: Company[];

	function navigate(name: string) {
		window.location.href = `/adtech/companies/${name}`;
	}
</script>

<div class="table-container">
	<table class="table table-hover table-auto">
		<thead>
			<tr>
				<th><h3 class="h3">Name</h3></th>
				<th><h3 class="h3">Count</h3></th>
				<th><h3 class="h3">Percentage</h3></th>
			</tr>
		</thead>
		<tbody>
			{#each Object.entries(tabledata) as [_prop, values]}
				<tr on:click={() => navigate(values.name)} style="cursor: pointer;">
					<td
						><div class="inline-flex">
							<h3 class="h4 md:h3">
								{values.name}
							</h3>
						</div>
					</td>
					<td>
						<div class="inline-flex">
							<h3 class="h4 md:h3 p-2">{values.app_count}</h3>
						</div>
					</td>
					<td>
						<div class="inline-flex">
							<h3 class="h4 md:h3 p-2">{`${(values.percent * 100).toFixed(1)}%`}</h3>
						</div>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
