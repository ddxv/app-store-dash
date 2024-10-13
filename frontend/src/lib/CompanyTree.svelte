<script lang="ts">
	import type { ParentCompanyTree } from '../types';
	import CompanyButton from './CompanyButton.svelte';
	import ExternalLink from './ExternalLink.svelte';

	export let myTree: ParentCompanyTree;
</script>

<div class="bg-white shadow-sm rounded-lg overflow-hidden">
	<div class="p-4 text-xs">
		<ul class="space-y-2">
			{#each myTree.children_companies as child}
				<li class="flex items-center space-x-2">
					<CompanyButton companyName={child.company_name} />
					{#each child.domains as domain}
						{#if domain}
							<div class="h-6 w-px bg-gray-300"></div>
							<ExternalLink {domain} />
						{/if}
					{/each}
				</li>
			{/each}
		</ul>
	</div>
</div>
