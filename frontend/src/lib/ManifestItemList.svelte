<script lang="ts">
	import type { Networks } from '../types';
	import type { Trackers } from '../types';

	export let title: string;
	export let items: Record<string, string[]> | Trackers | Networks = {};

	import CompanyButton from './CompanyButton.svelte';

	const androidNameFont = 'h6 px-8 md:px-16';
	const xmlPathFont = 'h5 px-4 md:px-8';
</script>

<h4 class="h4 md:h3 p-2 md:p-4 mt-4">{title}</h4>
<div class="px-2 md:px-4 max-w-sm lg:max-w-full overflow-x-scroll">
	<ul>
		{#each Object.entries(items) as [key, value]}
			{#if Array.isArray(value)}
				<!-- For leftovers -->
				<li>
					<p class={xmlPathFont}>{key}</p>
					<ul>
						{#each value as androidName}
							<li><p class={androidNameFont}>{androidName}</p></li>
						{/each}
					</ul>
				</li>
			{:else}
				<!-- For trackers and networks -->
				<div class="mt-4">
					<CompanyButton companyName={key} />
				</div>
				{#each Object.entries(value) as [xml_path, androidNames]}
					<li>
						<p class={xmlPathFont}>{xml_path}</p>
						{#if Array.isArray(androidNames)}
							<ul>
								{#each androidNames as androidName}
									<li><p class={androidNameFont}>{androidName}</p></li>
								{/each}
							</ul>
						{/if}
					</li>
				{/each}
			{/if}
		{/each}
	</ul>
</div>
