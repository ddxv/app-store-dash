<script lang="ts">
	import AdtechNav from '$lib/AdtechNav.svelte';
	$: entityGroup = 'networks';
</script>

<svelte:head>
	<title>Ad {entityGroup} stats</title>
	<meta
		name="description"
		content="Explore top advertising networks and third party trackers data across the mobile ad ecosystem for ios and android."
	/>
</svelte:head>

<div class="card p-2 md:p-16">
	<h3 class="h4 md:h3 p-4">Third Party Mobile Ad Tech Partners</h3>
	<AdtechNav></AdtechNav>
</div>
