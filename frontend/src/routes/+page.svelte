<script lang="ts">
	import AppRankTableShort from '$lib/AppRankTableShort.svelte';
	import type { HomeData } from '../types';

	export let data: HomeData;
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
	<div class="card p-2 md:p-8">
		<a href="/about">
			<h1 class="h1 p-2 md:p-4">AppGoblin: Mobile App Store Data and Stats</h1>
			<p class="p-2 md:p-4">
				AppGoblin is an open source project for collecting Google & Apple App Store data and
				presenting it for developers and marketers. AppGoblin features app store daily ranks and
				stats about mobile ad networks, data analytics tools, MMPs and app-ads.txt stats.<strong>
					Click here to learn more or request new features.</strong
				>
			</p>
		</a>
	</div>

	<br />

	<div class="card p-2 md:p-8">
		<a href="/rankings/store/1/collection/1/category/1">
			<h1 class="h1 p-2 md:p-4">Latest App Store Ranks</h1>
			<p class="p-2 md:p-4">Click through for full app store categories and rankings.</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			{#await data.androidAppRanks}
				Loading Android App Ranks...
			{:then androidApps}
				<a href="/rankings/store/1/collection/1/category/1">
					<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56">
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
					<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56">
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
					<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56">
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
					<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56">
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
	<div class="card p-2 md:p-8">
		<a href="/collections/new_monthly">
			<h1 class="h1 p-2 md:p-4">Most Integrated Ad Networks & Trackers</h1>
			<p class="p-2 md:p-4">
				By downloading and opening up the top apps and games from the Google and iOS Appstore we can
				see which third-party ad networks and trackers are used across the various App Store
				categories. The lists include various ad networks, MMPs, tracking, analytics and other 3rd
				party services which likely collect app data. You can also help expand these lists.
			</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			<a href="/adtech/Google/networks?groupby=brands&metric=appcount">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Top Android Ad Networks</h3>
					</div>
				</div>
			</a>
			<a href="/adtech/Google/trackers?groupby=brands&metric=appcount">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Top Android MMPs & Ad Tracking</h3>
					</div>
				</div>
			</a>
			<a href="/adtech/Apple/networks?groupby=brands&metric=appcount">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Top iOS Ad Networks</h3>
					</div>
				</div>
			</a>
			<a href="/adtech/Apple/trackers?groupby=brands&metric=appcount">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Top iOS MMPs & Ad Tracking</h3>
					</div>
				</div>
			</a>
		</div>
	</div>

	<br />
	<div class="card p-2 md:p-8">
		<a href="/collections/new_monthly">
			<h1 class="h1 p-2 md:p-4">Explore New Apps</h1>
			<p class="p-2 md:p-4">
				<strong> Click here to see explore all categories.</strong>
			</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			<a href="/collections/new_weekly">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Week</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_monthly">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Month</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_yearly">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Year</h3>
					</div>
				</div>
			</a>
			<a href="/collections/top">
				<div class="snap-center shrink-0 card variant-ghost-surface w-48 md:w-56 md:p-4">
					<div class="table-container card-header">
						<h3 class="h3">Alltime Most Popular</h3>
					</div>
				</div>
			</a>
		</div>
	</div>
</div>
