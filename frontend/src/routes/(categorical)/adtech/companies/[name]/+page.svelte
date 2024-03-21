<script lang="ts">
	import type { CompanyApps } from '../../../../../types';
	export let data: CompanyApps;
	import AppsCard from '$lib/AppGroupCard.svelte';
</script>

<div>
	{#await data.results}
		<div>
			<span>Loading...</span>
		</div>
	{:then apps}
		{#if typeof apps == 'string'}
			Failed to load network's apps.
		{:else}
			<h1 class="h1 p-2">Apps using {apps.title}</h1>
			<p class="h4 p-4">
				These are the apps we currently have which have at least one reference to the network in
				their AndroidManifest.xml
			</p>
			<AppsCard {apps} />
			<p class="p-2" />
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
