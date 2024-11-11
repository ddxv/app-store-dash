<script lang="ts">
	import type { Snippet } from 'svelte';
	let { title, children }: { title?: Snippet; children: Snippet } = $props();
</script>

<div class="card preset-tonal rounded-lg overflow-hidden">
	{#if title}
		<div class="card-header text-2xl bg-surface-100-900 border-b border-gray-200-800 p-1 md:p-2">
			{@render title?.()}
		</div>
	{/if}
	<div class="card-content">
		{@render children()}
	</div>
</div>
