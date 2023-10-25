<script>
	import ExternalLinkSvg from '$lib/ExternalLinkSVG.svelte';
	/** @type {import('../[id]/$types').PageData} */
	export let data;
	import AppDetails from '$lib/RatingInstallsLarge.svelte';
</script>

{#if data}
	<!-- App Icon Title & Info -->
	<section class="grid grid-cols-1 md:grid-cols-2 gap-4">
		<div class="card p-8">
			<div class="card-header p-4">
				<div class="inline-flex">
					{#if data.myapp.icon_url_512}
						<img
							src={data.myapp.icon_url_512}
							alt={data.myapp.name}
							class="w-60 h-60"
							referrerpolicy="no-referrer"
						/>
					{/if}
					<div class="p-4">
						{#if data.myapp.installs && data.myapp.installs != 0}
							<AppDetails app={data.myapp} />
						{/if}
					</div>
				</div>
			</div>

			<div class="card-footer flex">
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
						<img class="w-60" src="/gp_en_badge_web_generic.png" alt={data.myapp.name} />
					</a>
				</div>
			</div>
			<br />
			<div class="w-max-full flex">
				<h1 class="h1 p-2 self-center">{data.myapp.rating}</h1>
				<div class="flex-1">
					{#each [...data.myapp.histogram].reverse() as count, index}
						<div class="flex bar-spacer">
							<span class="label">{data.myapp.histogram.length - index}★</span>
							<div class="bar-container">
								<div
									class="bar"
									style="width: {(count / data.myapp.rating_count_num) * 100}%"
									title="{index + 1} star: {count} ratings"
								/>
								<!-- <span class="count">{count}</span> -->
							</div>
						</div>
					{/each}
				</div>
			</div>

			<h4 class="h4">Additional Information</h4>
			<div class="p-4">
				<p>Category: {data.myapp.category}</p>
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
		<div>
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
	<a href="/">Back to Home</a>
{:else}
	<p>Loading...</p>
{/if}

<style>
	.bar-spacer {
		margin: 10px;
	}

	.bar-container {
		display: flex;
		align-self: center;
		align-items: center;
		background-color: gainsboro;
		flex-grow: 1; /*Allow the bar to grow and take available space */
		border-radius: 10px; /* Rounded corners */
		margin-left: 5px;
		padding: 0px;
	}

	.bar {
		height: 20px; /* Fixed height for each bar */
		background-color: #3498db;
		transition: width 0.3s ease;
		border-radius: 10px; /* Rounded corners */
		/* flex-grow: 1; Allow the bar to grow and take available space */
	}

	.label,
	.count {
		margin: 0 10px;
		font-size: 14px;
	}
</style>
