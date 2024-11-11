<script lang="ts">
	import IconiOS from './svg/IconiOS.svelte';
	import IconGoogle from './svg/IconGoogle.svelte';

	const buttonSelectedColor =
		'bg-white border-2 border-primary-100 rounded-t-md relative top-[1px]';

	const buttonDeselectedColor = 'btn';

	interface Props {
		values: any;
		localHomeCategorySelect: string;
	}

	let { values, localHomeCategorySelect = $bindable() }: Props = $props();

	let isSelected = $derived(checkSelected());

	function checkSelected() {
		console.log('localHomeCategorySelect', localHomeCategorySelect);
		console.log('values.id', values.id);
		return localHomeCategorySelect == values.id;
	}

	function setSelectedClass(isSelected: boolean) {
		return isSelected ? buttonSelectedColor : buttonDeselectedColor;
	}
</script>

<div class="flex w-full justify-between p-1 {setSelectedClass(isSelected)}">
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
