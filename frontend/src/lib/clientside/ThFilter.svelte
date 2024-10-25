<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables';
	import { check } from '@vincjo/datatables';
	export let handler: DataHandler;
	export let filterBy: string;
	let value: string;
</script>

<th>
	<input
		class="input text-sm w-full"
		type="text"
		placeholder="Filter"
		bind:value
		on:input={() => {
			if (filterBy) handler.filter(value, filterBy, check.isLike);
		}}
	/>
</th>
