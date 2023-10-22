<script>
	import Rating from '$lib/Rating.svelte';
	import IconDownload from '$lib/IconDownload.svelte';
	export let app; // Accept the app object as a prop
</script>

<div class="inline-block">
	<h5 class="h5 p-2">{app.name}</h5>
	<!-- Ratings: STARS (123) -->
	{#if app.rating_count != 0 && app.rating_count != 'N/A'}
		<div class="inline-flex p-1">
			<Rating total={5} size={20} rating={app.rating} />
			({app.rating_count})
		</div>
	{/if}
	<!-- Installs DownloadIcon 123-->
	{#if app.installs != 0 && app.installs != 'N/A'}
		<div class="block p-0">
			<div class="inline-flex">
				<IconDownload />
				{app.installs}
			</div>
		</div>
	{/if}
</div>
