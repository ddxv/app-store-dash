<script lang="ts">
	import { page } from '$app/stores';

	import ExternalLink from '$lib/ExternalLink.svelte';
	import CompanyButton from '$lib/CompanyButton.svelte';

	let { children, data } = $props();
	const { domain, category } = $page.params;

	let category_title: string = $state(category);
	let rel_link = $state(domain);

	if (!category) {
		category_title = ' | ';
		rel_link = domain;
	} else {
		category_title = category + ' | ';
		rel_link = `${domain}/${category}`;
	}

	let categoryName = $derived(getAppCategories($page.params.category));

	function getAppCategories(category: string) {
		if (category) {
			return category.split('_').map((c) => c.charAt(0).toUpperCase() + c.slice(1));
		} else {
			return 'All App Categories';
		}
	}

	let titleClass = 'h1 text-3xl font-bold text-primary-900-100';
	let titleSecondaryClass = 'text-xl font-bold text-primary-900-100 mr-2';
	let titleDividerClass = 'md:h-8 w-px bg-gray-300 mx-2';
</script>

<svelte:head>
	<title>{domain} {category_title} Company Profile & Analytics | AppGoblin</title>
	<meta
		name="description"
		content="{domain} {category_title} biggest apps by most users. Explore detailed analytics, market presence, and insights about {domain}'s role in the mobile ecosystem."
	/>
	<meta
		name="keywords"
		content="{domain}, {category_title}, adtech, advertising network, data tracking, mobile measurement, programmatic advertising, app-ads.txt, mobile advertising, ad tech analytics, AppGoblin"
	/>
	<meta
		property="og:title"
		content="{domain} {category_title} | Adtech Company Insights | AppGoblin Analytics"
	/>
	<meta
		property="og:description"
		content="Discover {domain}'s impact in the {category_title} adtech industry. Analyze data on their apps, market presence, and role in mobile advertising. Powered by AppGoblin's comprehensive adtech research."
	/>
	<meta
		name="twitter:title"
		content="{domain} {category_title} Company Apps | AppGoblin Insights"
	/>
	<meta
		name="twitter:description"
		content="Uncover insights on {domain}'s {category_title} adtech operations. Explore data on their apps, industry connections, and market influence in mobile advertising and data tracking."
	/>

	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content="https://appgoblin.info/" />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<link rel="canonical" href={$page.url.href} />
</svelte:head>

<div class="flex items-center mb-2">
	{#await data.companyTree}
		<span class="text-lg">Loading...</span>
	{:then myTree}
		{#if typeof myTree == 'string'}
			<h1 class={titleClass}>{domain}</h1>
			<p class="text-red-500">Failed to load company tree.</p>
		{:else if myTree}
			<div class="flex flex-col md:flex-row items-left md:items-center">
				{#if myTree.queried_company_domain}
					{#if myTree.parent_company_domain == myTree.queried_company_domain}
						<!-- IS PARENT COMPANY -->
						<h1 class={titleClass}>{myTree.parent_company_name} / Category: {categoryName}</h1>
						<div class={titleDividerClass}></div>
						<ExternalLink domain={myTree.parent_company_domain} />
					{:else}
						<h1 class={titleClass}>{myTree.queried_company_name} / {categoryName}</h1>
						<div class={titleDividerClass}></div>
						<ExternalLink domain={myTree.queried_company_domain} />
						<div class={titleDividerClass}></div>
						<!-- HAS PARENT COMPANY -->
						<span class="flex row">
							<h2 class={titleSecondaryClass}>Parent Company:</h2>
							<CompanyButton
								companyName={myTree.parent_company_name}
								companyDomain={myTree.parent_company_domain}
							/>
						</span>
					{/if}
				{/if}
			</div>
		{/if}
	{:catch error}
		<p class="text-red-500">{error.message}</p>
	{/await}
</div>

{@render children?.()}
