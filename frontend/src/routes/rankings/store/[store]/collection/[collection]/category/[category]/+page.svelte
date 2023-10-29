<script lang="ts">
	export let data;
</script>

Welcome!

{#if data.ranks}
	{#each Object.entries(data.ranks.categories) as [_key, cat]}
		_key={_key}
		cat={cat}
	{/each}
{/if}
