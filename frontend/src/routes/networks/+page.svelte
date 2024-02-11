<script lang="ts">
	import type { TopNetworksInfo } from '../../types';
	export let data: TopNetworksInfo;

	function navigate(tracker_name: string) {
		window.location.href = `/networks/${tracker_name}`;
	}
</script>

<svelte:head>
	<title>Ad Network Stats</title>
	<meta
		name="description"
		content="Explore top advertising network's stats and data across the mobile ad ecosystem."
	/>
</svelte:head>

<div class="card p-2 md:p-16">
	<h3 class="h4 md:h3 p-4">Mobile Ad Networks</h3>

	<p class="p-8">
		For an app to make money from advertising, the owner of the app will usually use an Ad Network
		to sell their apps's advertising space. These Ad Networks will require an SDK to be used to
		manage the ad itself. AppGoblin is scanning apps to get an idea of which apps use which
		networks. Currently this list is for Android APKs only.
	</p>

	{#await data.networks.streamed}
		Loading Ad Networks...
	{:then networks}
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
					{#each Object.entries(networks.networks) as [_prop, values]}
						<tr on:click={() => navigate(values.network_name)} style="cursor: pointer;">
							<td
								><div class="inline-flex">
									<h3 class="h4 md:h3">
										{values.network_name}
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
