<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables';
	import { check } from '@vincjo/datatables';
	interface Props {
		handler: DataHandler;
		filterBy: string;
	}

	let { handler, filterBy }: Props = $props();
	let value: string = $state();
</script>

<th>
	<input
		class="input text-sm w-full"
		type="text"
		placeholder="Filter"
		bind:value
		oninput={() => {
			if (filterBy) handler.filter(value, filterBy, check.isLike);
		}}
	/>
</th>
