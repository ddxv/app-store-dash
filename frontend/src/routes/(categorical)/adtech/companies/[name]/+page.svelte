<script lang="ts">
	import type { CompanyFullDetails } from '../../../../../types';
	import { page } from '$app/stores';
	const { name } = $page.params;
	export let data: CompanyFullDetails;
	import CompanyOverviewTable from '$lib/CompanyOverviewTable.svelte';

	// Add this function in your <script> section
	function formatNumber(num) {
		return new Intl.NumberFormat('en-US').format(num);
	}
</script>

<div class="card-content p-6 bg-white shadow-md rounded-lg">
	<h1 class="text-3xl font-bold mb-6 text-gray-800">{name}</h1>
	{#await data.companyDetails}
		<div class="flex justify-center items-center h-40">
			<span class="text-lg text-gray-600">Loading...</span>
		</div>
	{:then myData}
		{#if typeof myData == 'string'}
			<p class="text-red-500 text-center">Failed to load company details.</p>
		{:else if myData}
			<div class="mt-6 bg-white p-6 rounded-lg shadow-md">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Total Apps</h2>
				<p class="text-lg text-gray-700">
					Total: <span class="font-semibold text-gray-900">{formatNumber(myData.total_apps)}</span>
				</p>
			</div>

			<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-6">
				<!-- SDK Section -->
				<div class="bg-white p-6 rounded-lg shadow-md">
					<h2 class="text-xl font-bold text-gray-800 mb-4">SDK</h2>
					<p class="text-lg text-gray-700 mb-2">
						SDK data is derived by downloading the app's Android APK or iOS IPA file and unzipped.
						We then check the app's data for SDK signatures in paths, AndroidManifest.xml and the
						Info.plist. Many apps are unable to be zipped. Downloading and opening the APK or IPA
						takes time and resources thus the smaller totals.
					</p>
					<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
						<!-- Android SDK -->
						<div class="card variant-glass-surface">
							<div class="card-header">
								<p class="text-lg text-gray-700">
									Android: <span class="font-semibold text-gray-900"
										>{formatNumber(myData.sdk_android_total_apps)}</span
									>
								</p>
							</div>
							<div class="card-content">
								{#await data.companyOverview}
									<div><span>Loading...</span></div>
								{:then tableData}
									{#if typeof tableData == 'string'}
										Failed to load company's apps.
									{:else if tableData}
										<CompanyOverviewTable entries_table={tableData.sdk.android.apps} />
									{:else}
										Failed to load company overview.
									{/if}
								{:catch error}
									<p style="color: red">{error.message}</p>
								{/await}
							</div>
						</div>
						<!-- iOS SDK -->
						<div class="card variant-glass-surface">
							<div class="card-header">
								<p class="text-lg text-gray-700">
									iOS: <span class="font-semibold text-gray-900"
										>{formatNumber(myData.sdk_ios_total_apps)}</span
									>
								</p>
							</div>
							<div class="card-content">
								{#await data.companyOverview}
									<div><span>Loading...</span></div>
								{:then tableData}
									{#if typeof tableData == 'string'}
										Failed to load company's apps.
									{:else if tableData}
										<CompanyOverviewTable entries_table={tableData.sdk.ios.apps} />
									{:else}
										Failed to load company overview.
									{/if}
								{:catch error}
									<p style="color: red">{error.message}</p>
								{/await}
							</div>
						</div>
					</div>
				</div>

				<!-- App Ads.txt Section -->
				<div class="bg-white p-6 rounded-lg shadow-md">
					<h2 class="text-xl font-bold text-gray-800 mb-4">App Ads.txt</h2>
					<p class="text-lg text-gray-700 mb-2">
						App-ads.txt files are an open standard by the IAB to help combat ad fraud. This data was
						crawled from the URLs on the app's developer pages. Not all apps have app-ads.txt, many
						do not.
					</p>
					<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
						<!-- Android App Ads.txt -->
						<div class="card variant-glass-surface">
							<div class="card-header">
								<p class="text-lg text-gray-700">
									Android: <span class="font-semibold text-gray-900"
										>{formatNumber(myData.adstxt_android_total_apps)}</span
									>
								</p>
							</div>
							<div class="card-content">
								{#await data.companyOverview}
									<div><span>Loading...</span></div>
								{:then tableData}
									{#if typeof tableData == 'string'}
										Failed to load company's apps.
									{:else if tableData}
										<CompanyOverviewTable entries_table={tableData.adstxt.android.apps} />
									{:else}
										Failed to load company overview.
									{/if}
								{:catch error}
									<p style="color: red">{error.message}</p>
								{/await}
							</div>
						</div>
						<!-- iOS App Ads.txt -->
						<div class="card variant-glass-surface">
							<div class="card-header">
								<p class="text-lg text-gray-700">
									iOS: <span class="font-semibold text-gray-900"
										>{formatNumber(myData.adstxt_ios_total_apps)}</span
									>
								</p>
							</div>
							<div class="card-content">
								{#await data.companyOverview}
									<div><span>Loading...</span></div>
								{:then tableData}
									{#if typeof tableData == 'string'}
										Failed to load company's apps.
									{:else if tableData}
										<CompanyOverviewTable entries_table={tableData.adstxt.ios.apps} />
									{:else}
										Failed to load company overview.
									{/if}
								{:catch error}
									<p style="color: red">{error.message}</p>
								{/await}
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</div>
