<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';

	export let baseUrl: string;

	$: console.log('MYURL', baseUrl);

	import IconGoogle from '$lib/svg/IconGoogle.svelte';
	import IconiOS from '$lib/svg/IconiOS.svelte';

	import { homeCollectionSelection } from '../stores';
	let localHomeCollectionSelect = $homeCollectionSelection;
	// Reactive statement to update the store when localValue changes
	$: homeCollectionSelection.set(localHomeCollectionSelect);

	import { homeStoreSelection } from '../stores';
	let localHomeStoreSelect = $homeStoreSelection;
	$: homeStoreSelection.set(localHomeStoreSelect);

	import { homeCategorySelection } from '../stores';
	let localHomeCategorySelect = $homeCategorySelection;
	const buttonSelectedColor = 'variant-filled-primary';
	$: homeCategorySelection.set(localHomeCategorySelect);

	import type { CatData } from '../types';

	const scrollTop = () => {
		const elemPage = document.querySelector('#page');
		if (elemPage !== null) {
			elemPage.scrollTop = 0;
		}
	};

	$: if ($page.params.category) {
		localHomeCategorySelect = $page.params.category;
	}

	export let myCatData: CatData;
</script>

<div class="p-1 md:p-2">
	<div class="card p-4">
		<h3 class="h4 md:h3">Categories</h3>
		<ListBox>
			{#if myCatData}
				{#each Object.entries(myCatData.categories) as [_prop, values]}
					{#if values.id && (Number(values.android) > 0 || values.name == 'Games')}
						<a href="{baseUrl}/{values.id}">
							<ListBoxItem
								bind:group={localHomeCategorySelect}
								name="medium"
								value={values.id}
								active={buttonSelectedColor}
								padding="p-2 md:p-2"
							>
								<div class="flex w-full justify-between">
									<div class="flex-grow">
										{values.name}
									</div>

									{#if Number(values.android) > 0 || values.name == 'Games'}
										<div class="justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconGoogle size="10" />
										</div>
									{/if}
									{#if Number(values.ios) > 0}
										<div class="justify-end mr-2 md:mr-5">
											<IconiOS size="10" />
										</div>
									{:else}
										<div class="opacity-20 justify-end mr-2 md:mr-5">
											<IconiOS size="10" />
										</div>
									{/if}
								</div>
							</ListBoxItem>
						</a>
					{/if}
				{/each}
			{/if}
		</ListBox>
	</div>
</div>
