<script lang="ts">
	import { idStoreSelection } from '../../stores';
	import { idCategorySelection } from '../../stores';
	import { idCollectionSelection } from '../../stores';

	import { storeIDLookup, collectionIDLookup, categoryIDLookup } from '../../stores';
</script>

<h1 class="h1 p-4">Welcome! Rankings</h1>
<h2 class="h2 p-2">Store! {storeIDLookup[$idStoreSelection].store_name}</h2>
<h2 class="h2 p-2">
	{#if collectionIDLookup[$idStoreSelection][$idCollectionSelection]}
		Collection! {collectionIDLookup[$idStoreSelection][$idCollectionSelection].collection_name}
		<h2 class="h2 p-2">
			Categories! {categoryIDLookup[$idCollectionSelection][$idCategorySelection].category_name}
		</h2>
	{/if}
</h2>

<div />
