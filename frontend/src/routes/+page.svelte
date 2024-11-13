<script lang="ts">
	import AppRankTableShort from '$lib/AppRankTableShort.svelte';
	import type { PageData } from './$types';

	import CompaniesBarChart from '$lib/CompaniesBarChart.svelte';
	import WhiteCard from '$lib/WhiteCard.svelte';

	let { data }: { data: PageData } = $props();

	function formatNumber(num: number) {
		return num.toLocaleString();
	}
</script>

<svelte:head>
	<!-- Title -->
	<title>AppGoblin: App Analytics & Market Trends | Google Play & iTunes</title>

	<!-- Standard meta tags -->
	<meta
		name="description"
		content="Discover app analytics and market trends for Google Play and iTunes with AppGoblin. Access detailed rankings, download statistics, and competitor insights to power your app strategy."
	/>
	<meta
		name="keywords"
		content="app analytics, market trends, Google Play data, iTunes app data, app rankings, download statistics, competitor analysis, mobile app insights, app store intelligence"
	/>

	<!-- Open Graph meta tags -->
	<meta
		property="og:title"
		content="AppGoblin: App Analytics & Market Trends for Google Play & iTunes"
	/>
	<meta
		property="og:description"
		content="Uncover app market trends, track rankings, and analyze competitors with AppGoblin's analytics for Google Play and iTunes. Make data-driven decisions for your app strategy."
	/>
	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content="https://appgoblin.info" />
	<meta property="og:type" content="website" />

	<!-- Twitter Card meta tags -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta
		name="twitter:title"
		content="AppGoblin: App Analytics & Market Trends | Google Play & iTunes"
	/>
	<meta
		name="twitter:description"
		content="Explore app market trends, track rankings, and analyze competitors with AppGoblin's app analytics for Google Play Android and iOS Appstore."
	/>
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />

	<!-- Additional meta tags -->
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta name="robots" content="index, follow" />
	<link rel="canonical" href="https://appgoblin.info" />
</svelte:head>

<div class="p-2 md:p-4 px-2 md:px-20 lg:px-48">
	<br />
	<div class="card preset-tonal-surface p-2 md:p-8">
		<h1 class="h1 p-2 md:p-4 text-primary-900-100">AppGoblin: Mobile App Store Data and Stats</h1>
		<p class="p-2 md:p-4">
			AppGoblin is an open source project for collecting Google & Apple App Store data and
			presenting it for developers and marketers. AppGoblin features app store daily ranks and stats
			about mobile ad networks, data analytics tools, MMPs and app-ads.txt stats.
		</p>
		<a href="/about" class="p-2 md:p-4">
			<strong> Click here to learn more or request new features.</strong>
		</a>

		<WhiteCard>
			{#snippet title()}
				App Store Scanned Apps
			{/snippet}
			{#await data.appsOverview}
				Loading Overview...
			{:then appsOverview}
				<div class="table-wrap">
					<table class="table w-full">
						<thead>
							<tr class="border-b">
								<th>Android Apps</th>
								<th>iOS Apps</th>
								<th>Android Weekly Scans</th>
								<th>iOS Weekly Scans</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>{formatNumber(appsOverview.android_apps)}</td>
								<td>{formatNumber(appsOverview.ios_apps)}</td>
								<td>{formatNumber(appsOverview.weekly_scanned_android_apps)}</td>
								<td>{formatNumber(appsOverview.weekly_scanned_ios_apps)}</td>
							</tr>
						</tbody>
					</table>
				</div>
			{:catch}
				Error Loading Overview
			{/await}
		</WhiteCard>
	</div>

	<br />

	<div class="card preset-tonal-surface p-2 md:p-8">
		<h2 class="h2 p-2 md:p-4">Latest App Store Ranks</h2>
		<a href="/rankings/store/1/collection/1/category/1">
			<p class="p-2 md:p-4">Click through for full app store categories and rankings.</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			{#await data.androidAppRanks}
				Loading Android App Ranks...
			{:then androidApps}
				<a href="/rankings/store/1/collection/1/category/1">
					<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">Android Apps</h3>
							<AppRankTableShort myTable={androidApps} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble Loading Android App Ranks.
			{/await}

			{#await data.iOSAppRanks}
				Loading iOS App Ranks...
			{:then iOSApps}
				<a href="/rankings/store/2/collection/4/category/120">
					<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">iOS Apps</h3>
							<AppRankTableShort myTable={iOSApps} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble Loading iOS App Ranks.
			{/await}

			{#await data.androidGameRanks}
				Loading Android Game Ranks...
			{:then androidGames}
				<a href="/rankings/store/1/collection/1/category/36">
					<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">Android Games</h3>
							<AppRankTableShort myTable={androidGames} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble loading android games
			{/await}

			{#await data.iOSGameRanks}
				Loading iOS Game Ranks...
			{:then iOSGames}
				<a href="/rankings/store/2/collection/4/category/62	">
					<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">iOS Games</h3>
							<AppRankTableShort myTable={iOSGames} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble Loading iOS Game Ranks.
			{/await}
		</div>
	</div>
	<br />
	<div class="card preset-tonal-surface p-2 md:p-8">
		<h2 class="h2 p-2 md:p-4">Most Integrated Ad Networks & Trackers</h2>
		<p class="p-2 md:p-4">
			By downloading and opening up the top apps and games from the Google and iOS Appstore we can
			see which third-party ad networks and trackers are used across the various App Store
			categories. The lists include various ad networks, MMPs, tracking, analytics and other 3rd
			party services which likely collect app data. You can also help expand these lists.
			<a href="/companies">
				<strong>Check out all the SDKs, Companies and Ad Network rankings.</strong>
			</a>
		</p>
		{#await data.appsOverview}
			Loading Overview...
		{:then appsOverview}
			<div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-2 md:p-4">
				<WhiteCard>
					{#snippet title()}
						Apps Checked for SDKs
					{/snippet}

					<table class="table">
						<thead>
							<tr class="border-b">
								<th>Total Apps</th>
								<th>Android Apps Scanned This Week</th>
								<th>iOS Apps Scanned This Week</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>{formatNumber(appsOverview.sdk_android_apps + appsOverview.sdk_ios_apps)}</td>
								<td>
									<span class="text-success-900-100">
										{formatNumber(appsOverview.sdk_weekly_success_android_apps)}
									</span>
									/{formatNumber(appsOverview.sdk_weekly_android_apps)}
								</td>
								<td>
									<span class="text-success-900-100">
										{formatNumber(appsOverview.sdk_weekly_success_ios_apps)}
									</span>
									/{formatNumber(appsOverview.sdk_weekly_ios_apps)}
								</td>
							</tr>
						</tbody>
					</table>
				</WhiteCard>

				<WhiteCard>
					{#snippet title()}
						App Ads URLs
					{/snippet}
					<table class="table mt-4">
						<thead>
							<tr class="border-b">
								<th>Total URLs</th>
								<th>URLs Scanned This Week</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>
									<span class="text-success-900-100">
										{formatNumber(appsOverview.appads_success_urls)}
									</span>
									/{formatNumber(appsOverview.appads_urls)}
								</td>

								<td>
									<span class="text-success-900-100">
										{formatNumber(appsOverview.appads_weekly_success_urls)}
									</span>
									/{formatNumber(appsOverview.appads_weekly_urls)}
								</td>
							</tr>
						</tbody>
					</table>
				</WhiteCard>
			</div>
		{:catch}
			Error Loading Overview
		{/await}

		<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
			<a href="/companies/types/ad-networks">
				<div class="card preset-tonal-surface md:p-4">
					<div class="card-header">
						<h3 class="h3">Top SDK Advertising Networks</h3>
					</div>
					<div class="card-content">
						Checkout the top SDK advertising networks.
						{#await data.topCompanies}
							Loading ...
						{:then myTops}
							{#if myTops.adnetworks}
								<WhiteCard>
									<CompaniesBarChart
										plotData={myTops.adnetworks.sdk}
										plotTitle="Top SDK Ad Networks Companies"
									/>
								</WhiteCard>
							{/if}
						{/await}
					</div>
				</div>
			</a>

			<a href="/companies/types/ad-attribution">
				<div class="card preset-tonal-surface md:p-4">
					<div class="card-header">
						<h3 class="h3">Top iOS MMPs & Ad Tracking</h3>
					</div>
					<div class="card-content">
						Checkout the top MMPs and tracking companies.
						{#await data.topCompanies}
							Loading ...
						{:then myTops}
							{#if myTops.attribution}
								<WhiteCard>
									<CompaniesBarChart
										plotData={myTops.attribution.sdk}
										plotTitle="Top MMPs & Attribution Companies"
									/>
								</WhiteCard>
							{/if}
						{/await}
					</div>
				</div>
			</a>

			<a href="/companies/types/product-analytics">
				<div class="card preset-tonal-surface md:p-4">
					<div class="card-header">
						<h3 class="h3">Top Product Analytics</h3>
					</div>
					<div class="card-content">
						Checkout the top product analytics companies.
						{#await data.topCompanies}
							Loading ...
						{:then myTops}
							{#if myTops.analytics}
								<WhiteCard>
									<CompaniesBarChart
										plotData={myTops.analytics.sdk}
										plotTitle="Top Product Analytics Companies"
									/>
								</WhiteCard>
							{/if}
						{/await}
					</div>
				</div>
			</a>
		</div>
	</div>

	<br />
	<div class="card preset-tonal-surface p-2 md:p-8">
		<a href="/collections/new_monthly">
			<h2 class="h2 p-2 md:p-4">Explore New Apps</h2>
			<p class="p-2 md:p-4">
				<strong> Click here to see explore all categories.</strong>
			</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 md:flex-row flex-col px-4 py-10"
		>
			<a href="/collections/new_weekly">
				<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Week</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_monthly">
				<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Month</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_yearly">
				<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Year</h3>
					</div>
				</div>
			</a>
			<a href="/collections/top">
				<div class="snap-center shrink-0 card preset-tonal-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Alltime Most Popular</h3>
					</div>
				</div>
			</a>
		</div>
	</div>
</div>
