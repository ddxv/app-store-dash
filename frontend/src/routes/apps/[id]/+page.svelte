<script lang="ts">
	import ExternalLinkSvg from '$lib/svg/ExternalLinkSVG.svelte';
	import ManifestItemList from '$lib/ManifestItemList.svelte';
	import type { AppFullDetails } from '../../../types';
	import AppDetails from '$lib/RatingInstallsLarge.svelte';
	import AppPlot from '$lib/AppPlot.svelte';
	import AvailableOniOs from '$lib/svg/AvailableOniOS.svelte';
	import RankChart from '$lib/RankChart.svelte';
	import AppHistoryTable from '$lib/AppHistoryTable.svelte';
	import AdsTxtTable from '$lib/AdsTxtTable.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';
	interface Props {
		data: AppFullDetails;
	}
	import { page } from '$app/stores';

	let { data }: Props = $props();
	let sum = (arr: number[]) => arr.reduce((acc, curr) => acc + curr, 0);
</script>

<svelte:head>
	<link rel="canonical" href="https://appgoblin.info/apps/{$page.params.id}" />
	{#await data.myapp then myapp}
		{#if myapp.store_link.includes('google')}
			<title>{myapp.name} Android Trends | {myapp.developer_name} | AppGoblin App Data</title>
			<meta
				name="description"
				content="Explore {myapp.name} Android app's analytics and market trends on Google Play with AppGoblin. Developed by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your Android app strategy and discover top-performing apps."
			/>
			<meta
				name="keywords"
				content="{myapp.name}, {myapp.developer_name}, {myapp.developer_id}, {myapp.category} analytics, ads, market data, Android app rankings, app reviews, download statistics, Google Play data, app comparison, mobile app insights, Android"
			/>
			<meta
				property="og:title"
				content="{myapp.name} Android App Stats & Info - AppGoblin | {myapp.developer_name}"
			/>
			<meta
				property="og:description"
				content="Explore {myapp.name} Android app analytics and market trends on Google Play with AppGoblin. {myapp.name} by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your Android app strategy and discover top-performing apps."
			/>
			<meta
				name="twitter:title"
				content="{myapp.name} Android | {myapp.developer_name} | App Stats & Info - AppGoblin"
			/>
			<meta
				name="twitter:description"
				content="Explore {myapp.name} Android app analytics and market trends on Google Play with AppGoblin. {myapp.name} by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your Android app strategy and discover top-performing apps."
			/>
		{:else}
			<title>{myapp.name} iOS Trends | {myapp.developer_name} | AppGoblin App Data</title>
			<meta
				name="description"
				content="Explore {myapp.name} iOS app's analytics and market trends on the App Store with AppGoblin. Developed by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your iOS app strategy and discover top-performing apps."
			/>
			<meta
				name="keywords"
				content="{myapp.name}, {myapp.developer_name}, {myapp.developer_id}, {myapp.category} analytics, market data, iOS app rankings, app reviews, download statistics, App Store data, app comparison, mobile app insights, iOS"
			/>
			<meta
				property="og:title"
				content="{myapp.name} iOS | {myapp.developer_name} | App Stats & Info - AppGoblin"
			/>
			<meta
				property="og:description"
				content="Explore {myapp.name} iOS app analytics and market trends on the App Store with AppGoblin. {myapp.name} by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your iOS app strategy and discover top-performing apps."
			/>
			<meta
				name="twitter:title"
				content="{myapp.name} iOS | {myapp.developer_name} | App Stats & Info - AppGoblin "
			/>
			<meta
				name="twitter:description"
				content="Explore {myapp.name} iOS app analytics and market trends on the App Store with AppGoblin. {myapp.name} by {myapp.developer_name} (ID: {myapp.developer_id}). Dive into detailed app rankings and download statistics to inform your iOS app strategy and discover top-performing apps."
			/>
		{/if}
		<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
		<meta property="og:url" content="https://appgoblin.info/" />
		<meta property="og:type" content="website" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	{/await}
</svelte:head>

<section class="grid grid-flow-cols-1 md:grid-cols-2 md:gap-4 p-2">
	<!-- Column1: App Icon Title & Info -->
	<div class="card preset-filled-surface-100-900 p-0 lg:p-8">
		<div class="card-header p-2 md:p-4">
			{#await data.myapp}
				Loading app details...
			{:then myapp}
				<div class="inline-flex">
					{#if myapp.icon_url_512}
						<img
							src={myapp.icon_url_512}
							alt={myapp.name}
							class="w-32 h-32 sm:w-40 sm:h-40 md:w-48 md:h-48 lg:w-56 lg:h-56 xl:w-60 xl:h-60"
							referrerpolicy="no-referrer"
						/>
					{/if}
					<div class="p-4">
						{#if myapp.installs && myapp.installs != '0'}
							<AppDetails app={myapp} />
						{/if}
					</div>
				</div>

				<div class="block md:hidden"></div>
				{#if myapp.developer_id}
					<div class="p-2 md:py-2">
						<a href="/developers/{myapp.developer_id}">
							<div class="btn preset-tonal hover:preset-tonal-primary">
								<span>Developer: {myapp.developer_name}</span>
							</div>
						</a>
					</div>
				{/if}
				<div class="p-2 md:py-2">
					<a href="/categories/{myapp.category}">
						<div class="btn preset-tonal hover:preset-tonal-primary">
							<span>Category: {myapp.category}</span>
						</div>
					</a>
				</div>
			{/await}
		</div>

		<div class="card-footer md:flex">
			{#await data.myapp}
				Loading app details...
			{:then myapp}
				<div class="block">
					<p>Store ID: {myapp.store_id}</p>
					{#if myapp.developer_id}
						Developer: <a
							class="anchor inline-flex items-baseline"
							href={myapp.store_developer_link}
							target="_blank"
						>
							{myapp.developer_name}
							<ExternalLinkSvg />
						</a>
					{:else}
						<p>Developer Name: {myapp.developer_name}</p>
						<p>Developer ID: {myapp.developer_id}</p>
					{/if}
					{#if myapp.developer_url}
						<p>
							Developer URL:
							<a class="anchor inline-flex" href="https://{myapp.developer_url}" target="_blank">
								{myapp.developer_url}
								<ExternalLinkSvg />
							</a>
						</p>
					{/if}
					<p>App Last Updated on Store: {myapp.store_last_updated}</p>
					<p>App Last Crawled: {myapp.updated_at}</p>
				</div>
				<div class="ml-auto">
					<a class="anchor inline-flex items-baseline" href={myapp.store_link} target="_blank">
						{#if myapp.store_link.includes('google')}
							<img class="w-40 md:w-60" src="/gp_en_badge_web_generic.png" alt={myapp.name} />
						{:else}
							<AvailableOniOs />
						{/if}
					</a>
				</div>
			{/await}
		</div>
		<br />
		<div class="p-2 md:flex">
			{#await data.myapp}
				Loading app rating details...
			{:then myapp}
				<div class="self-center text-center">
					<h1 class="h1 p-2">{myapp.rating}★</h1>
					Ratings: {myapp.rating_count}
				</div>
			{/await}
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
								></div>
							</div>
						</div>
					{/each}
				{/await}
			</div>
		</div>

		<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
			<h4 class="h4 md:h3 p-2">Lastest Store Ranks</h4>
			{#await data.myranks}
				Loading app ranks...
			{:then ranks}
				{#if typeof ranks == 'string'}
					<p>
						No official ranks available for this app. This app is not ranked on the store's top 200
						apps for it's categories.
					</p>
				{:else}
					{#if ranks.latest && ranks.latest.length > 0}
						{#each ranks.latest as myrow}
							<div class="px-4">
								#{myrow.rank}
								in: {myrow.collection}
								{myrow.category}
								({myrow.crawled_date})
							</div>
						{/each}
					{/if}
					{#if ranks.history && ranks.history.length > 0}
						<div class="card preset-tonal mt-2 md:mt-4">
							<h4 class="h4 md:h3 p-2 mt-2">Store Ranks Historical</h4>
							<RankChart plotData={ranks.history} narrowBool={true} />
						</div>
					{:else}
						<p>No ranking data available for this app.</p>
					{/if}
				{/if}
			{:catch}
				<p>The server caught an error.</p>
			{/await}
		</div>
		{#await data.myhistory}
			Loading historical data...
		{:then histdata}
			{#if histdata.history_table}
				{#await data.myapp then myapp}
					<AppHistoryTable os={myapp.store_link} history_table={histdata.history_table} />
				{/await}
			{/if}
			{#if histdata.plot_data && histdata.plot_data.installs && histdata.plot_data.installs.length > 1}
				<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
					<h3 class="h4 md:h3 p-2">Average Daily Installs</h3>
					<AppPlot plotdata={histdata.plot_data.installs} plotType="installs" />
				</div>
			{/if}
			{#if histdata.plot_data && histdata.plot_data.ratings && histdata.plot_data.ratings.length > 1}
				<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
					<h3 class="h4 md:h3 p-2">Average Daily Reviews & Ratings</h3>
					<AppPlot plotdata={histdata.plot_data.ratings} plotType="ratings" />
				</div>
			{/if}
			{#if histdata.plot_data && histdata.plot_data.changes && histdata.plot_data.changes.length > 1}
				<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
					<h3 class="h4 md:h3 p-2">Rate of Change Week on Week</h3>
					<AppPlot plotdata={histdata.plot_data.changes} plotType="change" />
				</div>
			{/if}
		{/await}

		{#await data.myAdsTxt}
			Loading App-Ads.txt data...
		{:then adstxt}
			{#if adstxt.direct_entries && adstxt.direct_entries.length >= 1}
				<div class="card preset-tonal mt-2 md:mt-4 md:p-4">
					<h4 class="h4 md:h3 p-2 mt-2">Direct App-Ads.Txt</h4>
					<AdsTxtTable entries_table={adstxt.direct_entries} />
				</div>
			{/if}
			{#if adstxt.reseller_entries && adstxt.reseller_entries.length >= 1}
				<div class="card preset-tonal mt-2 md:mt-4 md:p-4">
					<h4 class="h4 md:h3 p-2 mt-2">Reseller App-Ads.Txt Entries</h4>
					<AdsTxtTable entries_table={adstxt.reseller_entries} />
				</div>
			{/if}
		{/await}
	</div>

	<!-- Column2: App Pictures -->
	<div class="card preset-filled-surface-100-900 p-2 md:p-8">
		<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
			<h4 class="h4 md:h3 p-2">Screenshots</h4>
			{#await data.myapp then myapp}
				{#if myapp.featured_image_url}
					<div>
						<img
							class="h-auto max-w-full rounded-lg p-4 mx-auto"
							src={myapp.featured_image_url}
							alt=""
						/>
					</div>
				{/if}
				<section class="grid grid-cols-2 md:grid-cols-3 gap-4">
					{#each [myapp.phone_image_url_1, myapp.phone_image_url_2, myapp.phone_image_url_3, myapp.tablet_image_url_1, myapp.tablet_image_url_2, myapp.tablet_image_url_3] as imageUrl}
						{#if imageUrl && imageUrl != 'null'}
							<div>
								<img class="h-auto max-w-full rounded-lg" src={imageUrl} alt="" />
							</div>
						{/if}
					{/each}
				</section>
			{/await}
		</div>
		<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
			<h4 class="h4 md:h3 p-2">Additional Information</h4>
			<div class="px-4 md:px-8">
				{#await data.myapp then myapp}
					<p>Free: {myapp.free}</p>
					<p>Price: {myapp.price}</p>
					<p>Size: {myapp.size || 'N/A'}</p>
					<p>Minimum Android Version: {myapp.minimum_android || 'N/A'}</p>
					<p>Developer Email: {myapp.developer_email || 'N/A'}</p>
					<p>Content Rating: {myapp.content_rating || 'N/A'}</p>
					<p>Ad Supported: {myapp.ad_supported || 'N/A'}</p>
					<p>In-App Purchases: {myapp.in_app_purchases || 'N/A'}</p>
					<p>Editor's Choice: {myapp.editors_choice || 'N/A'}</p>
					<p>Last Crawl Result: {myapp.crawl_result}</p>
					<p>First Released: {myapp.release_date}</p>
					<p>Store Last Updated: {myapp.store_last_updated}</p>
					<p>First Crawled: {myapp.created_at}</p>
				{/await}
			</div>
		</div>
		<div class="card preset-tonal p-2 md:p-8 mt-2 md:mt-4">
			<h4 class="h4 md:h3 p-2">Ad SDKs, Trackers & Permissions</h4>
			{#await data.myPackageInfo}
				Loading permissions and tracker data...
			{:then packageInfo}
				{#if typeof packageInfo == 'string'}
					<p>Permissions, SDKs and trackers info not yet available for this app.</p>
				{:else}
					{#if packageInfo.company_categories && Object.keys(packageInfo.company_categories).length > 0}
						{#await data.companyTypes}
							Loading company types...
						{:then myCompanyTypes}
							{#each Object.keys(packageInfo.company_categories) as category}
								<WhiteCard>
									{#snippet title()}
										{myCompanyTypes.types.find((x) => x.url_slug === category)?.name || category}
									{/snippet}
									<div class="p-2">
										<ManifestItemList items={packageInfo.company_categories[category]}
										></ManifestItemList>
									</div>
								</WhiteCard>
							{/each}
						{/await}
					{/if}
					{#if packageInfo.permissions && packageInfo.permissions.length > 0}
						<h4 class="h4 md:h3 p-2 md:p-4 mt-4">Permissions</h4>
						<div class="px-4 md:px-8 max-w-sm md:max-w-md lg:max-w-full overflow-x-scroll">
							{#each packageInfo.permissions as permission}
								<p>{permission}</p>
							{/each}
						</div>
					{/if}
					{#if packageInfo.leftovers && Object.keys(packageInfo.leftovers).length > 0}
						<h4 class="h4 md:h3 p-2 md:p-4 mt-4">Unknown SDKs and Services</h4>
						<ManifestItemList items={packageInfo.leftovers}></ManifestItemList>
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
