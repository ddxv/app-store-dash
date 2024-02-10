<script lang="ts">
	import type { TopTrackersInfo } from '../../types';
	export let data: TopTrackersInfo;
</script>

<svelte:head>
	<title>App Trackers Data</title>
	<meta
		name="description"
		content="Explore top advertising data tracking collectors and trackers across the mobile ecosystem."
	/>
</svelte:head>

<div class="card p-2 md:p-8">
	<h3 class="h4 md:h3 p-4">Trackers</h3>

	{#await data.mytrackers.streamed}
		Loading App Trackers...
	{:then trackers}
		<div class="p-2 md:p-4" />
		<div class="table-container">
			<table class="table table-hover table-auto">
				<thead>
					<tr>
						<th>Rank</th>
						<th>Name</th>
					</tr>
				</thead>
				<tbody>
					{#each Object.entries(trackers.trackers) as [_prop, values]}
						<tr>
							<td
								><div class="inline-flex">
									<h3 class="h4 md:h3">
										{values.tracker_name}
									</h3>
								</div>
							</td>
							<td>
								<div class="inline-flex">
									<h3 class="h4 md:h3 p-2">{values.count}</h3>
								</div>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{:catch}
		Problem loading data
	{/await}
</div>

<a href="/"><p>Back to Home</p></a>
