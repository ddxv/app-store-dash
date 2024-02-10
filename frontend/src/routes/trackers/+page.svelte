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

<div class="card p-2 md:p-16">
	<h3 class="h4 md:h3 p-4">Trackers</h3>

	<p class="p-8">
		Tracking users in apps for marketing purposes is much harder in apps than on the regular web.
		Therefor most apps use other services embedded in their APKs to track users. AppGoblin is
		scanning apps to get an idea of which apps use which trackers. Currently this list is for
		Android APKs only.
	</p>

	{#await data.trackers.streamed}
		Loading App Trackers...
	{:then trackers}
		<div class="p-2 md:p-8" />
		<div class="table-container">
			<table class="table table-hover table-auto">
				<thead>
					<tr>
						<th>Name</th>
						<th>Count</th>
						<th>Percentage</th>
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
	{:catch}
		Problem loading data
	{/await}
</div>

<a href="/"><p>Back to Home</p></a>
