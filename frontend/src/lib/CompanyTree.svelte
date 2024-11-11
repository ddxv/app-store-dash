<script lang="ts">
	import type { ParentCompanyTree } from '../types';
	import CompanyButton from './CompanyButton.svelte';
	import ExternalLink from './ExternalLink.svelte';

	interface Props {
		myTree: ParentCompanyTree;
	}

	let { myTree }: Props = $props();
</script>

<div class="card preset-tonal shadow-sm rounded-lg overflow-hidden">
	<div class="p-4 text-xs">
		<ul class="space-y-2">
			{#each myTree.children_companies as child}
				<li class="flex items-center space-x-2">
					{#each child.domains as domain}
						{#if domain}
							<CompanyButton companyName={child.company_name} companyDomain={domain} />
							<div class="h-6 w-px bg-gray-300"></div>
							<ExternalLink {domain} />
						{:else}
							{child.company_name} has no url defined
						{/if}
					{/each}
				</li>
			{/each}
		</ul>
	</div>
</div>
