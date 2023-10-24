<script>
	export let data;
	import AppDetails from '$lib/RatingInstalls.svelte';
	function getClass(app) {
		return app.featured_image_url && app.featured_image_url !== 'null' ? 'col-span-2' : '';
	}
	import { myStoreSelection } from '../../../stores';
	import { myCategorySelection } from '../../../stores';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<div>
	{#if data.myapps}
		<!-- {#each Object.keys(data.myapps) as key} -->
		<h1 class="h1 p-2">{data.myapps.title}</h1>
		{#each Object.entries(data.myapps.categories) as [_key, cat]}
			{#if cat.key == $myCategorySelection}
				<div class="card p-2">
					<h2 class="h2 p-4">{cat[$myStoreSelection].title}: {$myCategorySelection}</h2>
					<hr class="section-divider" />
					<section class="grid grid-cols-3 md:grid-cols-5 gap-4">
						{#each cat[$myStoreSelection].apps as app}
							<!-- {#each data.myapps[$myCollectionSelection][$myStoreSelection].apps as app} -->
							<a href={`/apps/${app.store_id}`} class={`card overflow-hidden ${getClass(app)}`}>
								<div class="app-item">
									<header>
										<div>
											<!-- Show Featured Image (spans 2 cols) -->
											{#if app.featured_image_url && app.featured_image_url != 'null'}
												<div class="justify-center">
													<img
														class="h-auto object-fill rounded-lg"
														src={app.featured_image_url}
														alt={app.name}
													/>
												</div>
												<div class="inline-flex text-left">
													<img
														class="h-auto w-1/4 p-3 rounded-lg"
														src={app.icon_url_512}
														alt={app.name}
													/>
													<AppDetails {app} />
												</div>
												<!-- Show Icon Only (smaller) -->
											{:else if app.tablet_image_url && app.tablet_image_url != 'null'}
												<div>
													<img
														class="h-auto max-w-full rounded-lg"
														src={app.phone_image_url_1}
														alt={app.name}
													/>
													<img
														class="h-auto w-1/4 rounded-lg"
														src={app.icon_url_512}
														alt={app.name}
													/>
												</div>
											{:else}
												<img
													class="h-auto max-w-full rounded-lg"
													src={app.icon_url_512}
													alt={app.name}
												/>
												<AppDetails {app} />
											{/if}
										</div>
									</header>
								</div>
							</a>
						{/each}
					</section>
				</div>
				<p class="p-2" />
			{/if}
		{/each}
	{:else}
		<p>Loading...</p>
		{data}
	{/if}
</div>

<style>
	/* Container Grid */
	/* .app-grid {
		display: grid;
		gap: 15px;
		grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
		padding: 20px;
	/* } 

	/* Individual App Container */
	.app-item {
		display: flex;
		flex-direction: column;
		align-items: center; /* Center items horizontally */
		justify-content: top; /* Center items vertically */
		text-align: center;
		border: 1px solid #e0e0e0; /* Optional border */
		padding: 5px;
		border-radius: 8px; /* Rounded corners */
		transition: transform 0.3s; /* Hover effect */
	}

	.app-item:hover {
		transform: scale(1.05); /* Zoom in effect on hover */
		box-shadow: 0 8px 8px rgba(0, 0, 0, 0.1); /* Shadow on hover */
	}
</style>
