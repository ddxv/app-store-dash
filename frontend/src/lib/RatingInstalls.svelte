<script lang="ts">
	import Rating from '$lib/Rating.svelte';
	import IconDownload from '$lib/svg/IconDownload.svelte';
	import type { AppFullDetail } from '../types';
	import IconGoogle from './svg/IconGoogle.svelte';
	import IconiOs from './svg/IconiOS.svelte';
	export let app: AppFullDetail; // Accept the app object as a prop
</script>

<div class="flex flex-1">
	<div>
		<h5 class="h5 p-2">{app.name}</h5>
		<!-- Ratings: STARS (123) -->
		{#if app.rating_count != '0' && app.rating_count != 'N/A'}
			<div class="inline-flex p-1">
				<Rating total={5} size={20} rating={app.rating} />
				({app.rating_count})
			</div>
		{/if}
		<!-- Installs DownloadIcon 123-->
		{#if app.installs != '0' && app.installs != 'N/A'}
			<div class="block p-0">
				<div class="inline-flex">
					<IconDownload />
					{app.installs}
				</div>
			</div>
		{/if}
	</div>
	<div class="flex flex-1 items-center justify-center">
		{#if app.store_link.includes('google.com')}
			<IconGoogle size="40" />
		{/if}
		{#if app.store_link.includes('apple.com')}
			<IconiOs size="40" />
		{/if}
	</div>
</div>
