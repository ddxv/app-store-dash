<script lang="ts">
	interface Props {
		companyName: string;
		companyDomain: string;
	}

	let { companyName, companyDomain }: Props = $props();
	const baseUrl = '/companies';
</script>

<p class="h4">
	<a class="btn preset-tonal hover:preset-tonal-primary" href={`${baseUrl}/${companyDomain}`}
		>{companyName}</a
	>
</p>
