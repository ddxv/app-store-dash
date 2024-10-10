<script lang="ts">
	export let companyName: string;
	export let localUrl: string;
</script>

<p class="h4 mt-4">
	<a class="btn hover:bg-primary-hover-token variant-ghost-primary" href={localUrl}>{companyName}</a
	>
</p>
