<script lang="ts">
	import type { TopTrackersInfo } from '../../types';
	export let data: TopTrackersInfo;

	function navigate(name: string) {
		window.location.href = `/trackers/${name}`;
	}
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

	{#await data.companies.streamed}
		Loading App Trackers...
	{:then trackers}
		<div class="p-2 md:p-8" />
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
					{#each Object.entries(trackers.companies) as [_prop, values]}
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
	{:catch}
		Problem loading data
	{/await}
</div>

<a href="/"><p>Back to Home</p></a>
