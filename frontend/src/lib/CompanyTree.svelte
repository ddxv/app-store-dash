<script lang="ts">
	import type { ParentCompanyTree } from '../types';
	import ExternalLinkSvg from './svg/ExternalLinkSVG.svelte';
	import { goto } from '$app/navigation';
	import CompanyButton from './CompanyButton.svelte';

	export let myTree: ParentCompanyTree;

	function navigateToCompany(companyName: string) {
		goto(`/adtech/companies/${encodeURIComponent(companyName)}`);
	}
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
					<a
						href={`https://${child.domain}`}
						target="_blank"
						rel="noopener noreferrer"
						class="text-gray-500 hover:text-gray-700 flex items-center"
					>
						<span>{child.domain}</span>
						<ExternalLinkSvg />
					</a>
				</li>
			{/each}
		</ul>
	</div>
</div>
