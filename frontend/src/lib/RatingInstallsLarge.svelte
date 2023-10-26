<script lang="ts">
	import Rating from '$lib/Rating.svelte';
	import IconDownload from '$lib/svg/IconDownload.svelte';
	import type { AppFullDetail } from '../types';
	export let app: AppFullDetail; // Accept the app object as a prop
</script>

<div class="inline-block">
	<h5 class="h2 p-2">{app.name}</h5>
	<!-- Installs DownloadIcon 123-->
	{#if app.installs != '0' && app.installs != 'N/A'}
		<div class="block p-2 h3">
			<div class="inline-flex">
				<IconDownload />
				{app.installs}
			</div>
		</div>
	{/if}

	<!-- Ratings: STARS (123) -->
	<Rating total={5} size={50} rating={app.rating} />
	{#if app.rating_count != '0' && app.rating_count != 'N/A'}
		<div>
			Ratings: {app.rating_count}
			<br />
			Reviews: {app.review_count}
		</div>
	{:else}
		Ratings not yet available
	{/if}
</div>
