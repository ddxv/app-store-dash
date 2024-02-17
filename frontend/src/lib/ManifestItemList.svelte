<script lang="ts">
	import type { Networks } from '../types';
	import type { Trackers } from '../types';

	export let title: string;
	export let items: Record<string, string[]> | Trackers | Networks = {};
	export let basePath: string = '';
</script>

<h4 class="h4 md:h3 p-2 md:p-4 mt-4">{title}</h4>
<div class="px-4 md:px-8">
	<ul>
		{#each Object.entries(items) as [key, value]}
			{#if Array.isArray(value)}
				<!-- For leftovers -->
				<li>
					<p class="h5 px-4 md:px-8">{key}</p>
					<ul>
						{#each value as androidName}
							<li><p class="px-8 md:px-16">{androidName}</p></li>
						{/each}
					</ul>
				</li>
			{:else}
				<!-- For trackers and networks -->
				<p class="h5 mt-4">
					<a
						class="btn hover:bg-primary-hover-token variant-ghost-primary"
						href={`/${basePath}/${key}`}>{key}</a
					>
				</p>
				{#each Object.entries(value) as [xml_path, androidNames]}
					<li>
						<p class="h6 px-4 md:px-8">{xml_path}</p>
						{#if Array.isArray(androidNames)}
							<ul>
								{#each androidNames as androidName}
									<li><p class="px-8 md:px-16">{androidName}</p></li>
								{/each}
							</ul>
						{/if}
					</li>
				{/each}
			{/if}
		{/each}
	</ul>
</div>
