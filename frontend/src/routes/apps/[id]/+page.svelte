<script>
	import ExternalLinkSvg from '../../ExternalLinkSVG.svelte';
	/** @type {import('../[id]/$types').PageData} */
	export let data;
	import Rating from '../../Rating.svelte';
</script>

<!-- Navbar component inclusion should be done here, I assume it's a Svelte component -->
<!-- <Navbar /> -->

{#if data}
	<div class="card p-8">
		<div class="card-header">
			<h1 class="h1">{data.myapp.name}</h1>
			{#if data.myapp.icon_url_512}
				<img src={data.myapp.icon_url_512} alt={data.myapp.name} class="app-icon" />
			{/if}
			<div>
				<Rating total={5} size={50} rating={data.myapp.rating} />
			</div>
		</div>
		<!-- If app_rating is another Svelte component -->
		<!-- <AppRating app={data.myapp} /> -->

		<div class="card-footer important-info">
			<p>Store: {data.myapp.store}</p>
			<span class="inline-flex items-baseline">
				Store Link: <a
					class="anchor inline-flex"
					href={data.myapp.store_link}
					target="_blank"
					rel="noopener noreferrer"
				>
					{data.myapp.store_link}
					<ExternalLinkSvg />
				</a>
			</span>
			<p>Store ID: {data.myapp.store_id}</p>
			{#if data.myapp.installs != 'N/A'}
				<p><strong>Installs:</strong> {data.myapp.installs}</p>
			{/if}
			<p><strong>Rating:</strong> {data.myapp.rating}</p>
			<p><strong>Ratings:</strong> {data.myapp.rating_count}</p>
			<p><strong>Reviews:</strong> {data.myapp.review_count}</p>
			{#if data.myapp.developer_id != 'N/A'}
				Developer: <a
					class="anchor inline-flex"
					href={`https://apps.apple.com/us/developer/-/id${data.myapp.developer_id}`}
				>
					{data.myapp.developer_name}
					<ExternalLinkSvg />
				</a>
			{:else}
				<p>Developer Name: {data.myapp.developer_name}</p>
			{/if}

			<p>Developer ID: {data.myapp.developer_id}</p>
			<p>Developer URL: {data.myapp.developer_url}</p>
			<p>Store Last Crawled: {data.myapp.updated_at}</p>
		</div>
		<br />

		<h2 class="h2">Additional Information</h2>
		<div class="additional-info">
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

		<h2 class="h2">Historical Information</h2>
		<div class="additional-info">
			<!-- ... display additional information details -->
		</div>
	</div>

	<!-- <h2>Historical Information</h2>
<div class="additional-info">
	{@html data.myapp.history}
</div> -->

	<a href="/">Back to Home</a>
{:else}
	<p>Loading...</p>
{/if}

<style>
	.important-info {
		font-size: 1.2em;
		margin-bottom: 20px;
	}

	.additional-info {
		background-color: #f7f7f7;
		padding: 10px;
		border-radius: 5px;
	}

	.additional-info p {
		margin: 5px 0;
	}

	.app-icon {
		width: 256px;
		height: 256px;
		vertical-align: middle;
		margin-right: 10px;
	}

	.app-header {
		display: flex;
		align-items: center;
	}
</style>
