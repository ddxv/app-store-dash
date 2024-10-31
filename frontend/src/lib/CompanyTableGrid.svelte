<!-- @migration-task Error while migrating Svelte code: This migration would change the name of a slot making the component unusable -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-6">
	<!-- SDK Section -->
	<div class="bg-white p-2 md:p-6 rounded-lg shadow-md">
		<h2 class="text-xl font-bold text-gray-800 mb-4">SDK</h2>
		<p class="text-sm md:text-lg text-gray-700 mb-2">
			SDK data is derived by downloading the app's Android APK or iOS IPA file and unzipped. We then
			check the app's data for SDK signatures in paths, AndroidManifest.xml and the Info.plist. Many
			apps are unable to be zipped. Downloading and opening the APK or IPA takes time and resources
			thus the smaller totals.
		</p>
		<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
			<!-- Android SDK -->
			<div class="card variant-glass-surface">
				<div class="card-header">
					<p class="text-lg text-gray-700">
						<slot name="sdk-android-total-apps">Android Apps:</slot>
					</p>
				</div>
				<div class="card-content">
					<slot name="sdk-android" />
				</div>
			</div>
			<!-- iOS SDK -->
			<div class="card variant-glass-surface">
				<div class="card-header">
					<p class="text-lg text-gray-700">
						<slot name="sdk-ios-total-apps">iOS Apps:</slot>
					</p>
				</div>
				<div class="card-content">
					<slot name="sdk-ios" />
				</div>
			</div>
		</div>
	</div>

	<!-- App Ads.txt Section -->
	<div class="bg-white p-2 md:p-6 rounded-lg shadow-md">
		<h2 class="text-xl font-bold text-gray-800">App Ads.txt</h2>
		<p class="text-sm md:text-lg font-bold text-gray-800 mb-4">('DIRECT')</p>
		<p class="text-sm md:text-lg text-gray-700 mb-2">
			App-ads.txt files are an open standard by the IAB to help combat ad fraud. This data was
			crawled from the URLs on the app's developer pages. Not all apps have app-ads.txt, many do
			not.
		</p>
		<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
			<!-- Android App Ads.txt -->
			<div class="card variant-glass-surface">
				<div class="card-header">
					<p class="text-sm md:text-lg text-gray-700">
						<slot name="adstxt-android-total-apps">Android Apps:</slot>
					</p>
				</div>
				<div class="card-content">
					<slot name="adstxt-android" />
				</div>
			</div>
			<!-- iOS App Ads.txt -->
			<div class="card variant-glass-surface">
				<div class="card-header">
					<p class="text-sm md:text-lg text-gray-700">
						<slot name="adstxt-ios-total-apps">iOS Apps:</slot>
					</p>
				</div>
				<div class="card-content">
					<slot name="adstxt-ios" />
				</div>
			</div>
		</div>
	</div>
</div>
