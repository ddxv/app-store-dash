<script lang="ts">
	import type { AppGroup } from '../types';
	import type { AppFullDetail } from '../types';
	export let apps: AppGroup;

	import AppInfo from './RatingInstalls.svelte';

	function getClass(app: AppFullDetail) {
		return (app.featured_image_url && app.featured_image_url !== 'null') ||
			(app.tablet_image_url_1 && app.tablet_image_url_1 !== 'null')
			? 'col-span-2'
			: '';
	}
</script>

<div class="card p-2">
	<section class="grid grid-cols-1 md:grid-cols-4 gap-8">
		{#each apps.apps as app}
			<a
				href={`/apps/${app.store_id}`}
				class={`card variant-glass-secondary card-hover overflow-hidden ${getClass(app)}`}
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
									<AppInfo {app} />
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
										<AppInfo {app} />
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
										<AppInfo {app} />
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
									<AppInfo {app} />
								</div>
							{/if}
						</div>
					</header>
				</div>
			</a>
		{/each}
	</section>
</div>
