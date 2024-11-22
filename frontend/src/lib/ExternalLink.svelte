<script lang="ts">
	import ExternalLinkSvg from './svg/ExternalLinkSVG.svelte';
	interface Props {
		domain: string;
	}

	let { domain }: Props = $props();
</script>

<a href={`https://${domain}`} target="_blank" rel="noopener noreferrer" class="flex items-center">
	<span class="inline-flex items-center gap-1 text-tertiary-400-600 hover:text-primary-900-100">
		{domain}
		<ExternalLinkSvg />
	</span>
</a>
