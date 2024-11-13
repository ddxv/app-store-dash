<script lang="ts">
	import SideBar from '$lib/SideBar.svelte';
	import { Modal } from '@skeletonlabs/skeleton-svelte';

	let drawerState = $state(false);

	let { myCatData } = $props();

	function drawerClose() {
		drawerState = false;
	}
</script>

<!--
Tips for Drawer modals:
- Use `contentBase` to set styles, incuding height/width
- Set justify-start to align to the left
- Clear the align and padding styles
- Use `positionerClasses` to set the
- Set transition.x values that matches content width in pixels
-->

<Modal
	bind:open={drawerState}
	triggerBase="btn preset-tonal-primary"
	contentBase="bg-surface-100-900 space-y-4 shadow-xl h-screen overflow-y-scroll"
	positionerJustify="justify-start"
	positionerAlign=""
	positionerPadding=""
	transitionsPositionerIn={{ x: -480, duration: 200 }}
	transitionsPositionerOut={{ x: -480, duration: 200 }}
>
	{#snippet trigger()}APP FILTERS{/snippet}
	{#snippet content()}
		<SideBar {myCatData} />
		<footer>
			<button type="button" class="btn preset-filled" onclick={drawerClose}>Close</button>
		</footer>
	{/snippet}
</Modal>
