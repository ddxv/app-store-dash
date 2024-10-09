<script lang="ts">
	import type { ParentCompanyTree } from '../types';

	export let myTree: ParentCompanyTree;
	export let title = 'Subsidiary Companies';
</script>

<div class="bg-gray-100 p-6 rounded-lg shadow-lg">
	<h2 class="text-2xl font-bold text-gray-800 mb-6">{title}</h2>

	<div class="bg-white shadow-sm rounded-lg overflow-hidden">
		<div class="px-4 py-3 bg-gray-50 border-b border-gray-200">
			<h3 class="text-sm font-semibold text-gray-900">{myTree.parent_company_name}</h3>
		</div>
		<div class="p-4 text-xs">
			<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
				<div>
					<h4 class="font-medium text-gray-500 uppercase tracking-wider mb-1">
						Parent Company Details
					</h4>
					<p class="text-gray-700">Domain: {myTree.parent_company_domain}</p>
				</div>
				<div>
					<h4 class="font-medium text-gray-500 uppercase tracking-wider mb-1">
						Children Companies
					</h4>
					<ul class="list-disc list-inside space-y-0.5">
						{#each myTree.children_companies as child}
							<li class="text-gray-700">{child.company_name} ({child.domain})</li>
						{/each}
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
