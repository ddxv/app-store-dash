<script lang="ts">
	import ExternalLinkSvg from '$lib/svg/ExternalLinkSVG.svelte';
	import type { AppFullDetails } from '../../../types';
	export let data: AppFullDetails;
	import AppDetails from '$lib/RatingInstallsLarge.svelte';
	import AppPlot from '$lib/AppPlot.svelte';
	import AvailableOniOs from '$lib/svg/AvailableOniOS.svelte';
	import RankChart from '$lib/RankChart.svelte';
	import AppHistoryTable from '$lib/AppHistoryTable.svelte';
	let sum = (arr: number[]) => arr.reduce((acc, curr) => acc + curr, 0);
</script>

<svelte:head>
	{#await data.myapp.streamed}
		<title>App Stats & Info</title>
	{:then appdata}
		{#if typeof appdata == 'string'}
			<title>Not Found: App Stats & Info</title>
		{:else}
			<meta
				name="keywords"
				content=" {appdata.name}, app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
			/>
			<title>{appdata.name} App Stats & Info</title>
		{/if}
	{:catch}
		<title>Not Found: App Stats & Info</title>
	{/await}
	<meta
		name="description"
		content="Explore comprehensive app analytics and market trends across Google Play and iTunes with AppGoblin. Dive into detailed app rankings and download statistics to inform your app strategy and discover top-performing apps."
	/>
	<meta
		name="keywords"
		content="app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
	/>
</svelte:head>

{#await data.myapp.streamed}
	Loading App...
{:then appdata}
	{#if typeof appdata == 'string'}
		<p>We had trouble handling a server error. Please try again or try another app.</p>
	{:else}
		<!-- App Icon Title & Info -->
		<section class="grid grid-flow-cols-1 md:grid-cols-2 md:gap-4">
			<div class="card p-0 lg:p-8">
				<div class="card-header p-2 md:p-4">
					<div class="inline-flex">
						{#if appdata.icon_url_512}
							<img
								src={appdata.icon_url_512}
								alt={appdata.name}
								class="w-32 h-32 sm:w-40 sm:h-40 md:w-48 md:h-48 lg:w-56 lg:h-56 xl:w-60 xl:h-60"
								referrerpolicy="no-referrer"
							/>
						{/if}
						<div class="p-4">
							{#if appdata.installs && appdata.installs != '0'}
								<AppDetails app={appdata} />
							{/if}
						</div>
					</div>

					<div class="block md:hidden" />
					{#if appdata.developer_id}
						<div class="p-2 md:py-2">
							<a
								href="/developers/{appdata.developer_id}"
								class="btn hover:bg-primary-hover-token variant-ghost-primary"
								><span>Developer: {appdata.developer_name}</span></a
							>
						</div>
					{/if}
					<div class="p-2 md:py-2">
						<a
							href="/categories/{appdata.category}"
							class="btn hover:bg-primary-hover-token variant-ghost-primary"
							><span>Category: {appdata.category}</span></a
						>
					</div>
				</div>

				<div class="card-footer md:flex">
					<div class="block">
						<p>Store ID: {appdata.store_id}</p>
						{#if appdata.developer_id}
							Developer: <a
								class="anchor inline-flex items-baseline"
								href={appdata.store_developer_link}
								target="_blank"
							>
								{appdata.developer_name}
								<ExternalLinkSvg />
							</a>
						{:else}
							<p>Developer Name: {appdata.developer_name}</p>
							<p>Developer ID: {appdata.developer_id}</p>
						{/if}
						{#if appdata.developer_url}
							<p>
								Developer URL:
								<a
									class="anchor inline-flex"
									href="https://{appdata.developer_url}"
									target="_blank"
								>
									{appdata.developer_url}
									<ExternalLinkSvg />
								</a>
							</p>
						{/if}
						<p>Store Last Crawled: {appdata.updated_at}</p>
					</div>
					<div class="ml-auto">
						<a class="anchor inline-flex items-baseline" href={appdata.store_link} target="_blank">
							{#if appdata.store_link.includes('google')}
								<img class="w-40 md:w-60" src="/gp_en_badge_web_generic.png" alt={appdata.name} />
							{:else}
								<AvailableOniOs />
							{/if}
						</a>
					</div>
				</div>
				<br />
				<div class="p-2 md:flex">
					<div class="self-center text-center">
						<h1 class="h1 p-2">{appdata.rating}★</h1>
						Ratings: {sum(appdata.histogram)}
					</div>
					<div class="flex-1">
						{#each [...appdata.histogram].reverse() as count, index}
							<div class="flex bar-spacer">
								<span class="label">{appdata.histogram.length - index}★</span>
								<div class="bar-container flex-1">
									<div
										class="bar"
										style="width: {(count / sum(appdata.histogram)) * 100}%"
										title="{index + 1} star: {count} ratings"
									/>
								</div>
							</div>
						{/each}
					</div>
				</div>

				<h4 class="h4 md:h3 p-2 mt-2">Lastest Store Ranks</h4>
				{#await data.myranks.streamed}
					Loading ...
				{:then ranks}
					{#if typeof ranks == 'string'}
						<p>No ranks available for this app.</p>
					{:else}
						{#if ranks.latest && ranks.latest.length > 0}
							{#each ranks.latest as myrow}
								<h6 class="h6 px-4">
									#{myrow.rank}
									in: {myrow.collection}
									{myrow.category}
									({myrow.crawled_date})
								</h6>
							{/each}
						{/if}
						{#if ranks.history && ranks.history.length > 0}
							<div class="card variant-glass-surface mt-2 md:mt-4">
								<h4 class="h4 md:h3 p-2 mt-2">Store Ranks Historical</h4>
								<RankChart plotData={ranks.history} narrowBool={true} />
							</div>
						{:else}
							<p>No ranking data available for this app.</p>
						{/if}
					{/if}
				{/await}
				{#if appdata.history_table}
					<AppHistoryTable os={appdata.store_link} history_table={appdata.history_table} />
				{/if}
				{#if appdata.historyData && appdata.historyData.numbers && appdata.historyData.numbers.length > 1}
					<div class="card variant-glass-surface p-2 md:p-8 mt-2 md:mt-4">
						<h3 class="h4 md:h3 p-2">Avg Daily Counts</h3>
						<AppPlot plotdata={appdata.historyData.numbers} plotType="number" />
					</div>
					<div class="card variant-glass-surface p-2 md:p-8 mt-2 md:mt-4">
						<h3 class="h4 md:h3 p-2">Rate of Change Week on Week</h3>
						<AppPlot plotdata={appdata.historyData.changes} plotType="change" />
					</div>
				{/if}
			</div>
			<!-- App Pictures -->
			<div class="card p-8">
				<div class="card">
					{#if appdata.featured_image_url}
						<div>
							<img
								class="h-auto max-w-full rounded-lg p-4 mx-auto"
								src={appdata.featured_image_url}
								alt=""
							/>
						</div>
					{/if}
					<section class="grid grid-cols-2 md:grid-cols-3 gap-4">
						{#each [appdata.phone_image_url_1, appdata.phone_image_url_2, appdata.phone_image_url_3, appdata.tablet_image_url_1, appdata.tablet_image_url_2, appdata.tablet_image_url_3] as imageUrl}
							{#if imageUrl && imageUrl != 'null'}
								<div>
									<img class="h-auto max-w-full rounded-lg" src={imageUrl} alt="" />
								</div>
							{/if}
						{/each}
					</section>
				</div>
				<div class="p-2 md:p-8">
					<h4 class="h4 md:h3 p-2">Additional Information</h4>
					<div class="px-4 md:px-8">
						<p>Free: {appdata.free}</p>
						<p>Price: {appdata.price}</p>
						<p>Size: {appdata.size || 'N/A'}</p>
						<p>Minimum Android Version: {appdata.minimum_android || 'N/A'}</p>
						<p>Developer Email: {appdata.developer_email || 'N/A'}</p>
						<p>Content Rating: {appdata.content_rating || 'N/A'}</p>
						<p>Ad Supported: {appdata.ad_supported || 'N/A'}</p>
						<p>In-App Purchases: {appdata.in_app_purchases || 'N/A'}</p>
						<p>Editor's Choice: {appdata.editors_choice || 'N/A'}</p>
						<p>Last Crawl Result: {appdata.crawl_result}</p>
						<p>First Released: {appdata.release_date}</p>
						<p>Store Last Updated: {appdata.store_last_updated}</p>
						<p>First Crawled: {appdata.created_at}</p>
					</div>
				</div>
			</div>
		</section>
	{/if}
{:catch}
	<p>The server caught an error. Please try again or try another app.</p>
{/await}
<a href="/"><p>Back to Home</p></a>

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
