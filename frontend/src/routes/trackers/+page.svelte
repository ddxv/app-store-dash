<script lang="ts">
</script>

<svelte:head>
	<title>
		App Ranks {storeIDLookup[store].store_name}, Collection: {collectionIDLookup[store][collection]
			.collection_name}, Category: {categoryIDLookup[collection][category].category_name}
	</title>
	<meta
		name="description"
		content="Explore top advertising data collectors and trackers across the web."
	/>
</svelte:head>

<div class="card p-2 md:p-8">
	<h3 class="h4 md:h3 p-4">Trackers:</h3>

	{#await data.ranks.streamed}
		Loading App Ranks...
	{:then ranks}
		{#await data.history.streamed}
			Loading rank history...
		{:then history}
			<div class="card">
				<RankChart plotData={history.history} maxValue={10} />
			</div>
		{:catch}
			Failed to load history
		{/await}
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
					{#each Object.entries(ranks.ranks) as [_prop, values]}
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
											width="100 md:200"
											class="p-2"
											referrerpolicy="no-referrer"
										/>
										<h3 class="h4 md:h3 p-2">{values.name}</h3>
									</div>
								</a>
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
