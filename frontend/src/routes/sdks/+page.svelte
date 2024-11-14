<script lang="ts">
	import SDKsOverviewTable from '$lib/SDKsOverviewTable.svelte';
	let { data } = $props();
	import WhiteCard from '$lib/WhiteCard.svelte';
</script>

<h1 class="text-2xl font-bold text-primary-900-100">SDKs</h1>

<div class="my-6">
	<WhiteCard>
		{#snippet title()}
			SDKs Overview
		{/snippet}
		<p class="text-sm md:text-base p-2 md:p-4">
			These are the top SDK parts found from Android Manifests, Info.plist, directories and files.
			There is also a lot of other things mixed in, and much has yet to be tagged. If you see
			anything you'd like to tag please reach out on Discord to help contribute.
		</p>
	</WhiteCard>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-2 md:gap-6">
	{#await data.sdksOverview}
		loading
	{:then mySdksOverview}
		<WhiteCard>
			{#snippet title()}
				Android SDKs
			{/snippet}

			{#if mySdksOverview.android_overview.length > 0}
				<SDKsOverviewTable entries_table={mySdksOverview.android_overview} />
			{/if}
		</WhiteCard>

		<WhiteCard>
			{#snippet title()}
				iOS SDKs
			{/snippet}

			{#if mySdksOverview.ios_overview.length > 0}
				<SDKsOverviewTable entries_table={mySdksOverview.ios_overview} />
			{/if}
		</WhiteCard>
	{/await}
</div>
