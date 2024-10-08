<script lang="ts">
	import type { CompaniesOverview, CompaniesOverviewEntries } from '../../../../types';
	export let data: CompaniesOverview;
	import CompaniesOverviewTable from '$lib/CompaniesOverviewTable.svelte';
	console.log('HEIIIIIIIIIIIIIII');
</script>

<div>
	{#await data.companiesOverview}
		<div>
			<span>Loading...</span>
		</div>
	{:then apps}
		{#if typeof apps == 'string'}
			Failed to load network's apps.
		{:else}
			{console.log('HII11111111111111')}
			{#if apps}
				{console.log('HEIIIIIIIIIIIIIII2222222222')}
				<CompaniesOverviewTable entries_table={apps}></CompaniesOverviewTable>
				<p class="p-2" />
			{/if}
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
