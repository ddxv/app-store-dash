<script lang="ts">
	import { RadioGroup, RadioItem } from '@skeletonlabs/skeleton';
	import type { TopCompaniesInfo } from '../../types';
	export let data: TopCompaniesInfo;

	function navigate(name: string) {
		window.location.href = `/adtech/companies/${name}`;
	}
	let entityGroup = 'networks';
	let granularityGroup = 'brands';
</script>

<svelte:head>
	<title>Ad Network Stats</title>
	<meta
		name="description"
		content="Explore top advertising network's stats and data across the mobile ad ecosystem."
	/>
</svelte:head>

<div class="card p-2 md:p-16">
	<h3 class="h4 md:h3 p-4">Third Party Mobile Ad Tech Partners</h3>

	<div class="flex">
		<div class="card mx-4 p-4">
			<h3 class="h5 md:h4 p-4">Company Type</h3>
			<RadioGroup active="variant-filled-primary" hover="hover:variant-soft-primary">
				<RadioItem bind:group={entityGroup} name="entity" value="networks"
					>Advertising Networks</RadioItem
				>
				<RadioItem bind:group={entityGroup} name="entity" value="trackers"
					>Analytics, Attribution & MMPs</RadioItem
				>
			</RadioGroup>
		</div>
		<div class="card mx-4 p-4">
			<h3 class="h5 md:h4 p-4">Granularity</h3>
			<RadioGroup active="variant-filled-primary" hover="hover:variant-soft-primary">
				<RadioItem bind:group={granularityGroup} name="grouping" value="brands"
					>Group by brand</RadioItem
				>
				<RadioItem bind:group={granularityGroup} name="grouping" value="parents"
					>Group By Parent Company</RadioItem
				>
			</RadioGroup>
		</div>
	</div>
	{#if entityGroup === 'networks'}
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
						{#if granularityGroup == 'parents'}
							{#each Object.entries(networks.parent_companies) as [_prop, values]}
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
						{/if}
						{#if granularityGroup == 'brands'}
							{#each Object.entries(networks.companies) as [_prop, values]}
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
						{/if}
					</tbody>
				</table>
			</div>
		{:catch}
			Problem loading data
		{/await}
	{/if}
	{#if entityGroup === 'trackers'}
		{#await data.trackers.streamed}
			Loading Ad Trackers...
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
						{#if granularityGroup == 'parents'}
							{#each Object.entries(trackers.parent_companies) as [_prop, values]}
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
						{/if}
						{#if granularityGroup == 'brands'}
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
						{/if}
					</tbody>
				</table>
			</div>
		{:catch}
			Problem loading data
		{/await}
	{/if}
</div>

<a href="/"><p>Back to Home</p></a>
