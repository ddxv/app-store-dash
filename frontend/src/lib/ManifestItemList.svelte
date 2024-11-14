<script lang="ts">
	import type { Networks } from '../types';
	import type { Trackers } from '../types';
	import WhiteCard from './WhiteCard.svelte';
	import CompanyButton from './CompanyButton.svelte';
	interface Props {
		items?: Record<string, string[]> | Trackers | Networks;
	}

	let { items = {} }: Props = $props();

	const androidNameFont = 'text-xs md:text-sm px-8 md:px-16';
	const xmlPathFont = 'text-base px-4 md:px-8';
</script>

<div class="max-w-sm lg:max-w-full overflow-x-scroll">
	<ul>
		<div class="grid grid-cols-2 gap-2 md:gap-4">
			{#each Object.entries(items) as [key, value]}
				{#if Array.isArray(value)}
					<!-- For leftovers -->
					<li>
						<p class={xmlPathFont}>{key}</p>
						<ul>
							{#each value as androidName}
								<li><a href={`/sdks/${androidName}`} class={androidNameFont}>{androidName}</a></li>
							{/each}
						</ul>
					</li>
				{:else}
					<!-- For trackers and networks -->
					<WhiteCard>
						{#snippet title()}
							<div class="text-lg text-bold p-2">
								<CompanyButton companyName={key} companyDomain={key} />
							</div>
						{/snippet}
						{#each Object.entries(value) as [xml_path, androidNames]}
							<li>
								<p class={xmlPathFont}>{xml_path}</p>
								{#if Array.isArray(androidNames)}
									<ul>
										{#each androidNames as androidName}
											<li>
												<a href={`/sdks/${androidName}`} class={androidNameFont}>{androidName}</a>
											</li>
										{/each}
									</ul>
								{/if}
							</li>
						{/each}
					</WhiteCard>
				{/if}
			{/each}
		</div>
	</ul>
</div>
