<script lang="ts">
	import type { CompanyPatternsDict } from '../types';
	import WhiteCard from './WhiteCard.svelte';

	interface Props {
		mySdks: CompanyPatternsDict;
	}

	let { mySdks }: Props = $props();

	const uniquePaths = [
		...new Set(
			Object.values(mySdks.companies || {})
				.flatMap((c) => c.paths || [])
				.filter((path) => path != null)
		)
	];

	function truncateList(list: string[], maxItems = 3) {
		return list.slice(0, maxItems);
	}
</script>

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-2 md:p-4">
	{#each Object.entries(mySdks.companies) as [companyName, patterns]}
		<div class="col-span-1">
			<WhiteCard>
				{#snippet title()}
					<span class="text-sm font-semibold">{companyName}</span>
				{/snippet}
				<div class="p-4 text-xs">
					<h4 class="font-medium text-primary-900-100 uppercase tracking-wider mb-1">
						Package Patterns
					</h4>
					<ul class="list-disc list-inside space-y-0.5">
						{#each truncateList(patterns.package_patterns) as pattern}
							<li class=""><a href={`/sdks/${pattern}`}>{pattern}</a></li>
						{/each}
					</ul>
				</div>
			</WhiteCard>
		</div>
	{/each}

	<!-- Separate card for unique paths -->
	{#if uniquePaths.length > 0}
		<WhiteCard>
			{#snippet title()}
				<h3 class="text-sm font-semibold text-primary-900-100">Unique Path Patterns</h3>
			{/snippet}
			<div class="p-4 text-xs">
				<ul class="list-disc list-inside space-y-0.5">
					{#each truncateList(uniquePaths) as path}
						<li class="">{path}</li>
					{/each}
				</ul>
			</div>
		</WhiteCard>
	{/if}
</div>
