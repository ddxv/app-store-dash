<script lang="ts">
	import type { CompanyOverview } from '../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	export let data: CompanyOverview;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';
</script>

<div class="card p-4">
	<div class="card-header">Company Overview</div>
	<div class="card-content">
		<h1 class="h1 p-4">{name}</h1>
	</div>
	<div>
		{#await data.companyOverview}
			<div>
				<span>Loading...</span>
			</div>
		{:then myData}
			{#if typeof myData == 'string'}
				Failed to load company's apps.
			{:else if myData}
				<div class="flex gap-2">
					<div class="card variant-glass-surface">
						<div class="card-header">SDK Android</div>
						<div class="card-content">
							<CompanyOverviewTable entries_table={myData.sdk.android.apps}></CompanyOverviewTable>
						</div>
					</div>
					<div class="card variant-glass-surface">
						<div class="card-header">SDK iOS</div>
						<div class="card-content">
							<CompanyOverviewTable entries_table={myData.sdk.ios.apps}></CompanyOverviewTable>
						</div>
					</div>
					<p class="p-2" />
					<div class="card variant-glass-surface">
						<div class="card-header">Adstxt Android</div>
						<div class="card-content">
							<CompanyOverviewTable entries_table={myData.adstxt.android.apps}
							></CompanyOverviewTable>
						</div>
					</div>
					<div class="card variant-glass-surface">
						<div class="card-header">Adstxt iOS</div>
						<div class="card-content">
							<CompanyOverviewTable entries_table={myData.adstxt.ios.apps}></CompanyOverviewTable>
						</div>
					</div>
				</div>

				<p class="p-2" />
			{:else}
				Failed to load company overview.
			{/if}
		{:catch error}
			<p style="color: red">{error.message}</p>
		{/await}
	</div>
</div>
