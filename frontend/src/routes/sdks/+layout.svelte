<script lang="ts">
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();
</script>

<div class="p-2 md:p-8">
	{@render children?.()}
</div>
