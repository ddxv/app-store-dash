<script lang="ts">
	import {
		storeIDLookup,
		collectionIDLookup,
		categoryIDLookup
	} from '../../../../../../../../stores.js';

	export let data;

	import { page } from '$app/stores';

	$: store = +$page.params.store;
	$: collection = +$page.params.collection;
	$: category = +$page.params.category;
</script>

<h2 class="h2 p-4">
	Store: {storeIDLookup[store].store_name}, Collection: {collectionIDLookup[store][collection]
		.collection_name}, Category: {categoryIDLookup[collection][category].category_name}
</h2>

{#if data.ranks}
	<div class="table-container p-2 md:p-8">
		<table class="table table-hover table-auto">
			<thead>
				<tr>
					<th>Rank</th>
					<th>Name</th>
				</tr>
			</thead>
			<tbody>
				{#each Object.entries(data.ranks) as [_prop, values]}
					<tr>
						<td
							><div class="inline-flex">
								#
								<h2 class="h2">
									{values.rank}
								</h2>
							</div>
						</td>
						<td>
							<a href="/apps/{values.store_id}">
								<div class="inline-flex">
									<img src={values.icon_url_512} alt={values.name} width="50" class="p-2" />
									<h3 class="h3 p-2">{values.name}</h3>
								</div>
							</a>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{/if}
