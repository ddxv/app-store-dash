<script lang="ts">
	import { ListBoxItem } from '@skeletonlabs/skeleton';
	import IconiOS from './svg/IconiOS.svelte';
	import IconGoogle from './svg/IconGoogle.svelte';

	const buttonSelectedColor = 'variant-filled-primary';

	export let values: any;
	export let localHomeCategorySelect: string;
</script>

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
