<script lang="ts">
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();

	import { page } from '$app/stores';

	const { pattern } = $page.params;

	let sdk_title: string = $state(pattern);
</script>

<svelte:head>
	<title>{sdk_title} Mobile SDKs Libraries and Services | AppGoblin</title>
	<link rel="canonical" href="https://appgoblin.info/sdks/{pattern}" />
	<meta
		name="description"
		content="{sdk_title} is a mobile SDKs libraries and services. Explore detailed analytics, market presence, and insights about {sdk_title} in the mobile advertising ecosystem."
	/>
	<meta
		name="keywords"
		content="{sdk_title}, mobile SDKs, libraries, services, mobile advertising, data tracking, mobile measurement, programmatic advertising, app-ads.txt, mobile advertising, ad tech analytics, AppGoblin"
	/>
	<meta property="og:title" content="{sdk_title} Mobile SDKs Libraries and Services | AppGoblin" />
	<meta
		property="og:description"
		content="Discover {sdk_title}'s impact in the mobile adtech industry. Analyze data on their apps, market presence, and role in mobile advertising. Powered by AppGoblin's comprehensive adtech research."
	/>
	<meta name="twitter:title" content="{sdk_title} Mobile SDKs Libraries and Services | AppGoblin" />
	<meta
		name="twitter:description"
		content="Uncover insights on {sdk_title}'s mobile adtech operations. Explore data on their apps, industry connections, and market influence in mobile advertising and data tracking."
	/>

	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content="https://appgoblin.info/" />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
</svelte:head>

<div class="p-2 md:p-8">
	{@render children?.()}
</div>
