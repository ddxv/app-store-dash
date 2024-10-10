<script lang="ts">
	export let companyName: string;
	const baseUrl = '/adtech/companies';
</script>

<p class="h4">
	<a
		class="btn hover:bg-primary-hover-token variant-ghost-primary"
		href={`${baseUrl}/${companyName}`}>{companyName}</a
	>
</p>
