<script lang="ts">
	import type { Company } from '../types';
	export let tabledata: Company[];

	export let tableType: string = 'apps';

	function navigate(name: string) {
		window.location.href = `/adtech/companies/${name}`;
	}
</script>

<div class="table-container">
	<table class="table table-hover table-auto">
		<thead>
			<tr>
				<th><h4 class="h4">Name</h4></th>
				{#if tableType == 'apps'}
					<th><h4 class="h4">App Count</h4></th>
				{:else}
					<th><h4 class="h4">Installs</h4></th>
				{/if}
				<th><h4 class="h4">Percentage</h4></th>
			</tr>
		</thead>
		<tbody>
			{#each Object.entries(tabledata) as [_prop, values]}
				<tr on:click={() => navigate(values.name)} style="cursor: pointer;">
					<td
						><div class="inline-flex">
							<h3 class="h6 md:h5">
								{values.name}
							</h3>
						</div>
					</td>
					<td>
						<div class="inline-flex">
							{#if tableType == 'apps'}
								<h3 class="h6 md:h5">{values.app_count}</h3>
							{:else}
								<h3 class="h6 md:h5">{values.installs}</h3>
							{/if}
						</div>
					</td>
					<td>
						<div class="inline-flex">
							<h3 class="h6 md:h5">{`${(values.percent * 100).toFixed(1)}%`}</h3>
						</div>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
