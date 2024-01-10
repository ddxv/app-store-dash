<script lang="ts">
	import AppRankTableShort from '$lib/AppRankTableShort.svelte';
	import type { HomeData } from '../types';

	export let data: HomeData;
</script>

<div class="p-2 md:p-4 px-2 md:px-20 lg:px-48">
	<br />
	<div class="card p-2 md:p-8">
		<a href="/about">
			<h1 class="h1 p-2 md:p-4">AppGoblin for App Store Data and Stats</h1>
			<p class="p-2 md:p-4">
				App Goblin is an open source project for collecting Google & Apple App Store data and
				presenting it for developers and marketers to see how their app rankings. <strong>
					Click here to learn more.</strong
				>
			</p>
		</a>
	</div>

	<br />

	<div class="card p-2 md:p-8">
		<a href="/rankings/store/1/collection/1/category/1">
			<h1 class="h1 p-2 md:p-4">Track Latest Ranks</h1>
			<p class="p-2 md:p-4">Click through for full app store categories and rankings.</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			{#await data.androidAppRanks.streamed}
				Loading Android App Ranks...
			{:then androidApps}
				<a href="/rankings/store/1/collection/1/category/1">
					<div class="snap-center shrink-0 card w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">Android Apps</h3>
							<AppRankTableShort myTable={androidApps} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble Loading Android App Ranks.
			{/await}

			{#await data.iOSAppRanks.streamed}
				Loading iOS App Ranks...
			{:then iOSApps}
				<a href="/rankings/store/2/collection/4/category/55">
					<div class="snap-center shrink-0 card w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">iOS Apps</h3>
							<AppRankTableShort myTable={iOSApps} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble Loading iOS App Ranks.
			{/await}

			{#await data.androidGameRanks.streamed}
				Loading Android Game Ranks...
			{:then androidGames}
				<a href="/rankings/store/1/collection/1/category/36">
					<div class="snap-center shrink-0 card w-48 md:w-56">
						<div class="table-container card-header">
							<h3 class="h3">Android Games</h3>
							<AppRankTableShort myTable={androidGames} />
						</div>
					</div>
				</a>
			{:catch}
				Trouble loading android games
			{/await}

			{#await data.iOSGameRanks.streamed}
				Loading iOS Game Ranks...
			{:then iOSGames}
				<a href="/rankings/store/2/collection/4/category/62	">
					<div class="snap-center shrink-0 card w-48 md:w-56">
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
			<h1 class="h1 p-2 md:p-4">Explore New Apps</h1>
			<p class="p-2 md:p-4">
				<strong> Click here to see explore all categories.</strong>
			</p>
		</a>
		<div
			class="snap-x scroll-px-4 snap-mandatory scroll-smooth flex gap-4 overflow-x-auto px-4 py-10"
		>
			<a href="/collections/new_weekly">
				<div class="snap-center shrink-0 card w-48 md:w-56">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Week</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_monthly">
				<div class="snap-center shrink-0 card w-48 md:w-56">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Month</h3>
					</div>
				</div>
			</a>
			<a href="/collections/new_yearly">
				<div class="snap-center shrink-0 card w-48 md:w-56">
					<div class="table-container card-header">
						<h3 class="h3">Newest Apps This Year</h3>
					</div>
				</div>
			</a>
			<a href="/collections/top">
				<div class="snap-center shrink-0 card w-48 md:w-56">
					<div class="table-container card-header">
						<h3 class="h3">Alltime Most Popular</h3>
					</div>
				</div>
			</a>
		</div>
	</div>
</div>
