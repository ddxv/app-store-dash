<script>
	import { AppShell, ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	export let valueSingle = 'books';

	/** @type {import('./$types').PageData} */
	export let data;
	import Rating from './Rating.svelte';
</script>

<AppShell slotSidebarLeft="bg-surface-500/5 w-56 p-4">
	<svelte:fragment slot="sidebarLeft">
		<!-- Insert the list: -->
		<ListBox>
			<ListBoxItem bind:group={valueSingle} name="medium" value="google">Google</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="ios">iOS</ListBoxItem>
		</ListBox>
		<br />
		<hr class="!border-t-2" />
		Categories
		<ListBox>
			<ListBoxItem bind:group={valueSingle} name="medium" value="games">Games</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="apps">Apps</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
		</ListBox>

		<!-- --- -->
	</svelte:fragment>
	<h1>
		Welcome to My Apps Dash. Feel free to look around, if you have any questions just reach out or
		ping me on GitHub.
	</h1>
	<p>
		Visit <a href="https://github.com/ddxv/app-store-dash">github.com/ddxv/app-store-dash</a> to read
		the documentation
	</p>

	<div>
		{#if data}
			{#each Object.entries(data) as [title, collection]}
				<h1>{title}</h1>
				{#each Object.entries(collection) as [appstore, apps]}
					<h2>{appstore}</h2>
					<div class="app-grid">
						{#each apps as app}
							<div class="app-item">
								<a href={`/apps/${app.store_id}`} style="text-decoration: none; color: inherit;">
									<img src={app.icon_url_512} alt={app.name} class="app-icon" />
									<div>{app.name}</div>
									<Rating total={5} size={20} rating={app.rating} />
								</a>
							</div>
						{/each}
					</div>
					<hr class="section-divider" />
				{/each}
			{/each}
		{:else}
			<p>Loading...</p>
			{data}
		{/if}
	</div>
</AppShell>

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
		justify-content: center; /* Center items vertically */
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

	/* App Icons */
	.app-icon {
		width: 140px; /* Fixed width */
		height: 140px; /* Fixed height */
		margin-bottom: 10px; /* Space below icon */
		border-radius: 12px; /* Optional: Rounded corners for icons */
	}
</style>
