<script lang="ts">
	import ExternalLinkSvg from './svg/ExternalLinkSVG.svelte';
	interface Props {
		domain: string;
	}

	let { domain }: Props = $props();
</script>

<a
	href={`https://${domain}`}
	target="_blank"
	rel="noopener noreferrer"
	class="text-gray-500 hover:text-gray-700 flex items-center"
>
	<span class="inline-flex items-center gap-1">
		{domain}
		<ExternalLinkSvg />
	</span>
</a>
