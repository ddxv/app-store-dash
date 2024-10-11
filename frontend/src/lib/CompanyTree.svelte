<script lang="ts">
	import type { ParentCompanyTree } from '../types';
	import CompanyButton from './CompanyButton.svelte';
	import ExternalLink from './ExternalLink.svelte';

	export let myTree: ParentCompanyTree;
</script>

<div class="bg-white shadow-sm rounded-lg overflow-hidden">
	<div class="px-4 py-3 bg-gray-50 border-b border-gray-200">
		<h3 class="text-sm font-semibold text-gray-900">Subsidiary Companies</h3>
	</div>
	<div class="p-4 text-xs">
		<ul class="space-y-2">
			{#each myTree.children_companies as child}
				<li class="flex items-center space-x-2">
					<CompanyButton companyName={child.company_name} />
					<div class="h-6 w-px bg-gray-300"></div>
					{#each child.domains as domain}
						<ExternalLink {domain} />
					{/each}
				</li>
			{/each}
		</ul>
	</div>
</div>
