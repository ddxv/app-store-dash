<script lang="ts">
	export let companyName: string;
	export let companyDomain: string;
	const baseUrl = '/companies';
</script>

<p class="h4">
	<a
		class="btn hover:bg-primary-hover-token variant-ghost-primary"
		href={`${baseUrl}/${companyDomain}`}>{companyName}</a
	>
</p>
