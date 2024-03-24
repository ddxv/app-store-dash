<script lang="ts">
	import type { Company } from '../types';
	export let tabledata: Company[];

	export let tableType: string = 'apps';

	function navigate(name: string) {
		window.location.href = `/adtech/companies/${name}`;
	}

	function formatNumber(num: number) {
		if (num >= 1000000000000) return (num / 1000000000000).toFixed(1).replace(/\.0$/, '') + 'T';
		if (num >= 1000000000) return (num / 1000000000).toFixed(1).replace(/\.0$/, '') + 'B';
		if (num >= 1000000) return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
		if (num >= 1000) return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'K';
		return num;
	}
</script>

<div class="table-container px-0">
	<table class="table table-hover table-auto px-0">
		<thead class="px-0">
			<tr class="px-0">
				<th class="px-0"><h4 class="h4 px-0">Company</h4></th>
				{#if tableType == 'apps'}
					<th><h4 class="h4">App Count</h4></th>
				{:else}
					<th><h4 class="h4">Installs</h4></th>
				{/if}
				<th><h4 class="h4">Percent</h4></th>
			</tr>
		</thead>
		<tbody class="px-0">
			{#each Object.entries(tabledata) as [_prop, values]}
				<tr on:click={() => navigate(values.name)} style="cursor: pointer;" class="px-0">
					<td class="px-0"
						><div class="inline-flex">
							<h3 class="h7 md:h5">
								{values.name}
							</h3>
						</div>
					</td>
					<td>
						<div class="inline-flex">
							{#if tableType == 'apps'}
								<h3 class="h7 md:h5">{formatNumber(values.app_count)}</h3>
							{:else if values.installs}
								<h3 class="h7 md:h5">{formatNumber(values.installs)}</h3>
							{/if}
						</div>
					</td>
					<td>
						<div class="inline-flex">
							<h3 class="h7 md:h5">{`${(values.percent * 100).toFixed(1)}%`}</h3>
						</div>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
