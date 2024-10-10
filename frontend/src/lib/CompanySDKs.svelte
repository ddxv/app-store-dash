<script lang="ts">
	import type { CompanyPatternsDict } from '../types';

	export let title = 'Company SDKs';
	export let mySdks: CompanyPatternsDict;

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

<div class="bg-gray-100 p-6 rounded-lg shadow-lg">
	<h2 class="text-2xl font-bold text-gray-800 mb-6">{title}</h2>

	<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
		{#each Object.entries(mySdks.companies) as [companyName, patterns]}
			<div class="bg-white shadow-sm rounded-lg overflow-hidden">
				<div class="px-4 py-3 bg-gray-50 border-b border-gray-200">
					<h3 class="text-sm font-semibold text-gray-900">{companyName}</h3>
				</div>
				<div class="p-4 text-xs">
					<h4 class="font-medium text-gray-500 uppercase tracking-wider mb-1">Package Patterns</h4>
					<ul class="list-disc list-inside space-y-0.5">
						{#each truncateList(patterns.package_patterns) as pattern}
							<li class="text-gray-700">{pattern}</li>
						{/each}
					</ul>
				</div>
			</div>
		{/each}

		<!-- Separate card for unique paths -->
		{#if uniquePaths.length > 0}
			<div class="bg-white shadow-sm rounded-lg overflow-hidden">
				<div class="px-4 py-3 bg-gray-50 border-b border-gray-200">
					<h3 class="text-sm font-semibold text-gray-900">Unique Path Patterns</h3>
				</div>
				<div class="p-4 text-xs">
					<ul class="list-disc list-inside space-y-0.5">
						{#each truncateList(uniquePaths) as path}
							<li class="text-gray-700">{path}</li>
						{/each}
					</ul>
				</div>
			</div>
		{/if}
	</div>
</div>
