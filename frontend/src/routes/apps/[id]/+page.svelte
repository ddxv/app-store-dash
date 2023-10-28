<script lang="ts">
	import ExternalLinkSvg from '$lib/svg/ExternalLinkSVG.svelte';
	import type { AppFullDetails } from '../../../types';
	/** @type {import('../[id]/$types').PageData} */
	export let data: AppFullDetails;
	import AppDetails from '$lib/RatingInstallsLarge.svelte';
	import AppPlot from '$lib/AppPlot.svelte';
	import AvailableOniOs from '$lib/svg/AvailableOniOS.svelte';
	let sum = (arr: number[]) => arr.reduce((acc, curr) => acc + curr, 0);
</script>

{#if data.myapp}
	<!-- App Icon Title & Info -->
	<section class="grid grid-flow-cols-1 md:grid-cols-2 md:gap-4">
		<div class="card variant-glass-surface p-0 lg:p-8">
			<div class="card-header p-2 md:p-4">
				<div class="inline-flex">
					{#if data.myapp.icon_url_512}
						<img
							src={data.myapp.icon_url_512}
							alt={data.myapp.name}
							class="w-32 h-32 sm:w-40 sm:h-40 md:w-48 md:h-48 lg:w-56 lg:h-56 xl:w-60 xl:h-60"
							referrerpolicy="no-referrer"
						/>
					{/if}
					<div class="p-4">
						{#if data.myapp.installs && data.myapp.installs != '0'}
							<AppDetails app={data.myapp} />
						{/if}
					</div>
				</div>

				<div class="block md:hidden" />
				{#if data.myapp.developer_id}
					<a href="/developers/{data.myapp.developer_id}" class="btn variant-filled"
						><span>Developer: {data.myapp.developer_name}</span></a
					>
				{/if}
				<a href="/categories/{data.myapp.category}" class="btn variant-filled"
					><span>Category: {data.myapp.category}</span></a
				>
			</div>

			<div class="card-footer md:flex">
				<div class="block">
					<p>Store ID: {data.myapp.store_id}</p>
					{#if data.myapp.developer_id}
						Developer: <a
							class="anchor inline-flex items-baseline"
							href={data.myapp.store_developer_link}
							target="_blank"
						>
							{data.myapp.developer_name}
							<ExternalLinkSvg />
						</a>
					{:else}
						<p>Developer Name: {data.myapp.developer_name}</p>
						<p>Developer ID: {data.myapp.developer_id}</p>
					{/if}
					{#if data.myapp.developer_url}
						<p>
							Developer URL:
							<a
								class="anchor inline-flex"
								href="https://{data.myapp.developer_url}"
								target="_blank"
							>
								{data.myapp.developer_url}
								<ExternalLinkSvg />
							</a>
						</p>
					{/if}
					<p>Store Last Crawled: {data.myapp.updated_at}</p>
				</div>
				<div class="ml-auto">
					<a class="anchor inline-flex items-baseline" href={data.myapp.store_link} target="_blank">
						{#if data.myapp.store_link.includes('google')}
							<img class="w-40 md:w-60" src="/gp_en_badge_web_generic.png" alt={data.myapp.name} />
						{:else}
							<AvailableOniOs />
						{/if}
					</a>
				</div>
			</div>
			<br />
			<div class="p-2 md:flex">
				<div class="self-center text-center">
					<h1 class="h1 p-2">{data.myapp.rating}★</h1>
					Ratings: {sum(data.myapp.histogram)}
				</div>
				<div class="flex-1">
					{#each [...data.myapp.histogram].reverse() as count, index}
						<div class="flex bar-spacer">
							<span class="label">{data.myapp.histogram.length - index}★</span>
							<div class="bar-container flex-1">
								<div
									class="bar"
									style="width: {(count / sum(data.myapp.histogram)) * 100}%"
									title="{index + 1} star: {count} ratings"
								/>
							</div>
						</div>
					{/each}
				</div>
			</div>

			<h4 class="h4">Additional Information</h4>
			<div class="p-4">
				<p>Free: {data.myapp.free}</p>
				<p>Price: {data.myapp.price}</p>
				<p>Size: {data.myapp.size || 'N/A'}</p>
				<p>Minimum Android Version: {data.myapp.minimum_android || 'N/A'}</p>
				<p>Developer Email: {data.myapp.developer_email || 'N/A'}</p>
				<p>Content Rating: {data.myapp.content_rating || 'N/A'}</p>
				<p>Ad Supported: {data.myapp.ad_supported || 'N/A'}</p>
				<p>In-App Purchases: {data.myapp.in_app_purchases || 'N/A'}</p>
				<p>Editor's Choice: {data.myapp.editors_choice || 'N/A'}</p>
				<p>Last Crawl Result: {data.myapp.crawl_result}</p>
				<p>First Released: {data.myapp.release_date}</p>
				<p>Store Last Updated: {data.myapp.store_last_updated}</p>
				<p>First Crawled: {data.myapp.created_at}</p>
			</div>

			<h4 class="h4">Historical Information</h4>
			<div>
				{@html data.myapp.history_table}
			</div>
		</div>
		<!-- App Pictures -->
		<div class="card variant-glass-surface p-8">
			{#if data.myapp.featured_image_url}
				<div>
					<img
						class="h-auto max-w-full rounded-lg p-4 mx-auto"
						src={data.myapp.featured_image_url}
						alt=""
					/>
				</div>
			{/if}
			<section class="grid grid-cols-2 md:grid-cols-3 gap-4">
				{#each [data.myapp.phone_image_url_1, data.myapp.phone_image_url_2, data.myapp.phone_image_url_3, data.myapp.tablet_image_url_1, data.myapp.tablet_image_url_2, data.myapp.tablet_image_url_3] as imageUrl}
					{#if imageUrl && imageUrl != 'null'}
						<div>
							<img class="h-auto max-w-full rounded-lg" src={imageUrl} alt="" />
						</div>
					{/if}
				{/each}
			</section>
		</div>
	</section>
	<section>
		{#if data.myapp.historyData}
			<h1 class="h1">Plot</h1>
			<AppPlot plotdata={data.myapp.historyData} />
		{/if}
	</section>
	<a href="/">Back to Home</a>
{:else}
	<p>Loading...</p>
{/if}

<style>
	.bar-spacer {
		margin: 10px;
	}

	.bar-container {
		align-self: center;
		align-items: center;
		background-color: gainsboro;
		border-radius: 5px; /* Rounded corners */
		margin-left: 5px;
		padding: 0px;
	}

	.bar {
		height: 20px; /* Fixed height for each bar */
		background-color: #3498db;
		border-radius: 5px; /* Rounded corners */
		/* flex-grow: 1; Allow the bar to grow and take available space */
	}
</style>
