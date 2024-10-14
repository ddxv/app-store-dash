<script lang="ts">
	import { page } from '$app/stores';
	const { name, category } = $page.params;

	let category_title: string = category;
	let rel_link = name;

	if (!category) {
		category_title = ' | ';
		rel_link = name;
	} else {
		category_title = category + ' | ';
		rel_link = `${name}/${category}`;
	}
</script>

<svelte:head>
	<title>{name} {category_title} Adtech Company Profile & Analytics | AppGoblin</title>
	<meta
		name="description"
		content="{name} {category_title} is an adtech company with their apps in its network. Explore detailed analytics, market presence, and insights about {name}'s role in the mobile advertising ecosystem."
	/>
	<meta
		name="keywords"
		content="{name}, {category_title}, adtech, advertising network, data tracking, mobile measurement, programmatic advertising, app-ads.txt, mobile advertising, ad tech analytics, AppGoblin"
	/>
	<meta
		property="og:title"
		content="{name} {category_title} | Adtech Company Insights | AppGoblin Analytics"
	/>
	<meta
		property="og:description"
		content="Discover {name}'s impact in the {category_title} adtech industry. Analyze data on their apps, market presence, and role in mobile advertising. Powered by AppGoblin's comprehensive adtech research."
	/>
	<meta
		name="twitter:title"
		content="{name} {category_title} Adtech Profile | AppGoblin Insights"
	/>
	<meta
		name="twitter:description"
		content="Uncover insights on {name}'s {category_title} adtech operations. Explore data on their apps, industry connections, and market influence in mobile advertising and data tracking."
	/>

	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content="https://appgoblin.info/" />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<link rel="canonical" href="https://appgoblin.info/companies/{rel_link}" />
</svelte:head>

<slot></slot>
