<script lang="ts">
	import type { AppGroup } from '../types';
	import type { AppFullDetail } from '../types';

	import AppInfo from './RatingInstalls.svelte';
	interface Props {
		apps: AppGroup;
	}

	let { apps }: Props = $props();

	function getClass(app: AppFullDetail) {
		return (app.featured_image_url && app.featured_image_url !== 'null') ||
			(app.tablet_image_url_1 && app.tablet_image_url_1 !== 'null')
			? 'col-span-2'
			: '';
	}
</script>

<div class="card p-2 md:p-8">
	<h2 class="h3 md:h2 p-2 md:p-4">Apps: {apps.title}</h2>
	<section class="grid grid-col grid-flow-row md:grid-cols-4 gap-4 md:gap-8">
		{#each apps.apps as app}
			<a href={`/apps/${app.store_id}`} class={`card card-hover overflow-hidden ${getClass(app)}`}>
				<div>
					<header>
						<div>
							<!-- Show Featured Image (spans 2 cols) -->
							{#if app.featured_image_url && app.featured_image_url != 'null'}
								<div class="justify-center">
									<img
										class="h-48 w-full object-top object-none rounded-lg"
										src={app.featured_image_url}
										alt={app.name}
										referrerpolicy="no-referrer"
									/>
								</div>
								<div class="flex text-left">
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
									<div class="inline-flex mx-auto">
										<img
											class="h-48 w-48 p-3 rounded-lg"
											src={app.icon_url_512}
											alt={app.name}
											referrerpolicy="no-referrer"
										/>
										<img
											class="object-top object-cover h-48 w-48 rounded-lg"
											src={app.phone_image_url_1}
											alt={app.name}
											referrerpolicy="no-referrer"
										/>
									</div>
									<div class="inline-flex text-left">
										<img
											class="hidden md:inline-flex md:h-24 w-24 p-3 rounded-lg"
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
										class="h-48 w-48 rounded-lg mx-auto"
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
