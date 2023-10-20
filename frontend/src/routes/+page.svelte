<script>
	/** @type {import('./$types').PageData} */
	export let data;
	import Rating from './Rating.svelte';
</script>

<h1 class="h1 p-4">Welcome</h1>

<div>
	{#if data}
		{#each Object.entries(data) as [_prop, values]}
			{#each Object.entries(values) as [_collection, collectionData]}
				<div class="card p-2">
					<h1 class="h1 p-2">{collectionData.title}</h1>
					<hr class="section-divider" />
					{#each Object.entries(collectionData.data) as [_collection2, collectionData2]}
						<h2 class="h2 p-4">{collectionData2.title}</h2>
						<div class="app-grid">
							{#each collectionData2.apps as app}
								<a href={`/apps/${app.store_id}`} style="card overflow-hidden">
									<div class="app-item">
										<header>
											<img src={app.icon_url_512} alt={app.name} />
										</header>
										<div class="card-footer p-2">
											<h5 class="h5">{app.name}</h5>
											{#if app.rating_count != 0 && app.rating_count != null}
												<Rating total={5} size={20} rating={app.rating} />
												({app.rating_count})
											{/if}
										</div>
									</div>
								</a>
							{/each}
						</div>
					{/each}
				</div>
				<p class="p-2" />
			{/each}
		{/each}
	{:else}
		<p>Loading...</p>
		{data}
	{/if}
</div>

<style>
	/* Container Grid */
	.app-grid {
		display: grid;
		gap: 15px; /* Gap between grid items */
		grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
		padding: 20px; /* Padding around the entire grid */
	}

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
