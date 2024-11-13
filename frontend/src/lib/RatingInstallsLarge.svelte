<script lang="ts">
	import Rating from '$lib/Rating.svelte';
	import IconDownload from '$lib/svg/IconDownload.svelte';
	import type { AppFullDetail } from '../types';
	interface Props {
		app: AppFullDetail;
	}

	let { app }: Props = $props();
</script>

<div class="inline-block">
	<h1 class="h1 md:h2 p-0 md:p-2 text-primary-900-100">{app.name}</h1>
	<!-- Installs DownloadIcon 123-->
	{#if app.installs != '0' && app.installs != 'N/A'}
		<div class="block p-0 md:p-2 h3">
			<div class="inline-flex">
				<IconDownload />
				{app.installs}
			</div>
		</div>
	{/if}

	<!-- Ratings: STARS (123) -->
	<div class="md:hidden">
		<Rating total={5} size={25} rating={app.rating} />
	</div>
	<div class="hidden md:inline-flex">
		<Rating total={5} size={50} rating={app.rating} />
	</div>
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
