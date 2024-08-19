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
	import AppRankTable from '$lib/AppRankTable.svelte';

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
		<AppRankTable tableData={ranks}></AppRankTable>
	{:catch}
		Problem loading data
	{/await}
</div>

<a href="/"><p>Back to Home</p></a>
