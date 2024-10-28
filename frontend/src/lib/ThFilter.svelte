<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables/legacy/remote';
	interface Props {
		handler: DataHandler;
		filterBy: string;
	}

	let { handler, filterBy }: Props = $props();

	let value: string = $state();
	let timeout: any;

	const filter = () => {
		handler.filter(value, filterBy);
		clearTimeout(timeout);
		timeout = setTimeout(() => {
			handler.invalidate();
		}, 400);
	};
</script>

<th>
	<input
		class="input text-sm w-full"
		type="text"
		placeholder="Filter"
		bind:value
		oninput={filter}
	/>
</th>
