<script lang="ts">
	import {
		storeIDLookup,
		collectionIDLookup,
		categoryIDLookup
	} from '../../../../../../../../../stores.js';

	import type { StoreCategoryRanks } from '../../../../../../../../../types.js';

	export let data: StoreCategoryRanks;

	import { page } from '$app/stores';
	import RankChart from '$lib/RankChart.svelte';

	$: store = +$page.params.store;
	$: collection = +$page.params.collection;
	$: category = +$page.params.category;
</script>

<svelte:head>
	<title>
		App Ranks {storeIDLookup[store].store_name}, Collection: {collectionIDLookup[store][collection]
			.collection_name}, Category: {categoryIDLookup[collection][category].category_name}
	</title>
	<meta
		name="description"
		content="Explore comprehensive app rankings across Google Play and iTunes with AppGoblin. Dive into detailed app rankings and download statistics to inform your app strategy and discover top-performing apps."
	/>
</svelte:head>

<div class="card p-2 md:p-8">
	<h3 class="h4 md:h3 p-4">
		Store: {storeIDLookup[store].store_name}, Collection: {collectionIDLookup[store][collection]
			.collection_name}, Category: {categoryIDLookup[collection][category].category_name}
	</h3>

	{#await data.ranks}
		Loading App Ranks...
	{:then ranks}
		{#await data.history}
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
