<script>
	/** @type {import('../[collection]/$types').PageData} */
	export let data;
	import AppDetails from '$lib/RatingInstalls.svelte';
	function getClass(app) {
		return (app.featured_image_url && app.featured_image_url !== 'null') ||
			(app.tablet_image_url_1 && app.tablet_image_url_1 !== 'null')
			? 'col-span-2'
			: '';
	}

	import { myStoreSelection } from '../../../stores';
	import { myCategorySelection } from '../../../stores';

	import { myCategoryMap } from '../../../stores';
</script>

<h1 class="h1 p-4">Welcome!</h1>

<div>
	{#if data}
		<h1 class="h1 p-2">{data.myapps.title}</h1>
		{#each Object.entries(data.myapps.categories) as [_key, cat]}
			{#if cat.key == $myCategorySelection}
				<div class="card p-2">
					<h2 class="h2 p-4">
						{cat[$myStoreSelection].title}:
						{#if $myCategoryMap}
							{#each Object.entries($myCategoryMap.mycats.categories) as [_key, catMap]}
								{#if catMap.id == cat.key}
									{catMap.name}
								{/if}
							{/each}
						{:else}
							cat
						{/if}
					</h2>
					<hr class="section-divider" />
					<section class="grid grid-cols-3 md:grid-cols-4 gap-4">
						{#each cat[$myStoreSelection].apps as app}
							<a
								href={`/apps/${app.store_id}`}
								class={`card card-hover overflow-hidden ${getClass(app)}`}
							>
								<div>
									<header>
										<div>
											<!-- Show Featured Image (spans 2 cols) -->
											{#if app.featured_image_url && app.featured_image_url != 'null'}
												<div class="justify-center">
													<img
														class="h-48 w-full object-cover rounded-lg"
														src={app.featured_image_url}
														alt={app.name}
														referrerpolicy="no-referrer"
													/>
												</div>
												<div class="inline-flex text-left">
													<img
														class="h-24 w-24 p-3 rounded-lg"
														src={app.icon_url_512}
														alt={app.name}
														referrerpolicy="no-referrer"
													/>
													<AppDetails {app} />
												</div>
												<!-- Show Tablet -->
											{:else if app.tablet_image_url_1 && app.tablet_image_url_1 != 'null'}
												<div>
													<img
														class="object-top object-cover h-48 w-full rounded-lg"
														src={app.tablet_image_url_1}
														alt={app.name}
														referrerpolicy="no-referrer"
													/>
													<div class="inline-flex text-left">
														<img
															class="h-24 w-24 p-3 rounded-lg"
															src={app.icon_url_512}
															alt={app.name}
															referrerpolicy="no-referrer"
														/>
														<AppDetails {app} />
													</div>
												</div>
												<!-- Show Phone Screenshot -->
											{:else if app.phone_image_url_1 && app.phone_image_url_1 != 'null'}
												<div>
													<img
														class="object-top object-cover h-48 w-full rounded-lg"
														src={app.phone_image_url_1}
														alt={app.name}
														referrerpolicy="no-referrer"
													/>
													<div class="inline-flex text-left">
														<img
															class="h-24 w-24 p-3 rounded-lg"
															src={app.icon_url_512}
															alt={app.name}
															referrerpolicy="no-referrer"
														/>
														<AppDetails {app} />
													</div>
												</div>
												<!-- Show Icon Only (smaller) -->
											{:else}
												<div class="mx-auto block text-center">
													<img
														class="h-48 max-w-full rounded-lg mx-auto"
														src={app.icon_url_512}
														alt={app.name}
														referrerpolicy="no-referrer"
													/>
													<AppDetails {app} />
												</div>
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
