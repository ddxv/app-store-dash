<script>
	import { AppShell, ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	export let valueSingle = 'books';
</script>

<AppShell slotSidebarLeft="bg-surface-500/5 w-56 p-4">
	<svelte:fragment slot="sidebarLeft">
		<!-- Insert the list: -->
		<ListBox>
			<ListBoxItem bind:group={valueSingle} name="medium" value="google">Google</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="ios">iOS</ListBoxItem>
		</ListBox>
		<br />
		<hr class="!border-t-2" />
		Categories
		<ListBox>
			<ListBoxItem bind:group={valueSingle} name="medium" value="games">Games</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="apps">Apps</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
			<ListBoxItem bind:group={valueSingle} name="medium" value="tv">TV</ListBoxItem>
		</ListBox>

		<!-- --- -->
	</svelte:fragment>
</AppShell>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
