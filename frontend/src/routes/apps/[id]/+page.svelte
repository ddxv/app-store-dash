<script lang="ts">
	import ExternalLinkSvg from '$lib/svg/ExternalLinkSVG.svelte';
	import ManifestItemList from '$lib/ManifestItemList.svelte';
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
	<title>App Stats & Info</title>
	<meta
		name="keywords"
		content=" {data.myapp
			.name}, app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
	/>
	<title>{data.myapp.name} App Stats & Info</title>
	<meta
		name="description"
		content="Explore comprehensive app analytics and market trends across Google Play and iTunes with AppGoblin. Dive into detailed app rankings and download statistics to inform your app strategy and discover top-performing apps."
	/>
	<meta
		name="keywords"
		content="app analytics, app market data, mobile app rankings, app reviews, download statistics, Google Play data, iTunes app data, app comparison, mobile app insights"
	/>
</svelte:head>

<section class="grid grid-flow-cols-1 md:grid-cols-2 md:gap-4">
	<!-- Column1: App Icon Title & Info -->
	<div class="card p-0 lg:p-8">
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
				<div class="p-2 md:py-2">
					<a
						href="/developers/{data.myapp.developer_id}"
						class="btn hover:bg-primary-hover-token variant-ghost-primary"
						><span>Developer: {data.myapp.developer_name}</span></a
					>
				</div>
			{/if}
			<div class="p-2 md:py-2">
				<a
					href="/categories/{data.myapp.category}"
					class="btn hover:bg-primary-hover-token variant-ghost-primary"
					><span>Category: {data.myapp.category}</span></a
				>
			</div>
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
						<a class="anchor inline-flex" href="https://{data.myapp.developer_url}" target="_blank">
							{data.myapp.developer_url}
							<ExternalLinkSvg />
						</a>
					</p>
				{/if}
				<p>App Last Updated on Store: {data.myapp.store_last_updated}</p>
				<p>App Last Crawled: {data.myapp.updated_at}</p>
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
				Ratings: {data.myapp.rating_count}
			</div>
			<div class="flex-1">
				{#await data.myhistory}
					Loading rating details...
				{:then histdata}
					{#each [...histdata.histogram].reverse() as count, index}
						<div class="flex bar-spacer">
							<span class="label">{histdata.histogram.length - index}★</span>
							<div class="bar-container flex-1">
								<div
									class="bar"
									style="width: {(count / sum(histdata.histogram)) * 100}%"
									title="{index + 1} star: {count} ratings"
								/>
							</div>
						</div>
					{/each}
				{/await}
			</div>
		</div>

		<h4 class="h4 md:h3 p-2 mt-2">Lastest Store Ranks</h4>
		{#await data.myranks}
			Loading app ranks...
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
				{#await data.myhistory}
					Loading historical data...
				{:then histdata}
					{#if histdata.history_table}
						<AppHistoryTable os={data.myapp.store_link} history_table={histdata.history_table} />
					{/if}
					{#if histdata.plot_data && histdata.plot_data.numbers && histdata.plot_data.numbers.length > 1}
						<div class="card variant-glass-surface p-2 md:p-8 mt-2 md:mt-4">
							<h3 class="h4 md:h3 p-2">Avg Daily Counts</h3>
							<AppPlot plotdata={histdata.plot_data.numbers} plotType="number" />
						</div>
						<div class="card variant-glass-surface p-2 md:p-8 mt-2 md:mt-4">
							<h3 class="h4 md:h3 p-2">Rate of Change Week on Week</h3>
							<AppPlot plotdata={histdata.plot_data.changes} plotType="change" />
						</div>
					{/if}
				{/await}
			{/if}
		{:catch}
			<p>The server caught an error.</p>
		{/await}
	</div>

	<!-- Column2: App Pictures -->
	<div class="card p-8">
		<div class="card">
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
			<div class="p-2 md:p-4">
				<h4 class="h4 md:h3 p-2">Additional Information</h4>
				<div class="px-4 md:px-8">
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
			</div>
		</div>
		<div class="card">
			{#await data.myPackageInfo}
				Loading permissions and tracker data...
			{:then packageInfo}
				{#if typeof packageInfo == 'string'}
					<p>Permissions info not yet available for this app.</p>
				{:else}
					{#if packageInfo.permissions && packageInfo.permissions.length > 0}
						<h4 class="h4 md:h3 p-2 md:p-4 mt-4">Permissions</h4>
						<div class="px-4 md:px-8 max-w-sm md:max-w-md lg:max-w-full overflow-x-scroll">
							{#each packageInfo.permissions as permission}
								<p>{permission}</p>
							{/each}
						</div>
					{/if}
					{#if packageInfo.trackers && Object.keys(packageInfo.trackers).length > 0}
						<ManifestItemList items={packageInfo.trackers} title="Trackers" basePath="trackers"
						></ManifestItemList>
					{/if}
					{#if packageInfo.networks && Object.keys(packageInfo.networks).length > 0}
						<ManifestItemList items={packageInfo.networks} title="Ad Networks" basePath="networks"
						></ManifestItemList>
					{/if}
					{#if packageInfo.leftovers && Object.keys(packageInfo.leftovers).length > 0}
						<ManifestItemList items={packageInfo.leftovers} title="Other Services"
						></ManifestItemList>
					{/if}
				{/if}
			{/await}
		</div>
	</div>
</section>

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
