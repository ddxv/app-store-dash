<script>
	import { TabAnchor, TabGroup } from '@skeletonlabs/skeleton';
	import { marked } from 'marked';
	const url = 'https://raw.githubusercontent.com/ddxv/app-store-dash/main/README.md';
</script>

<h1 class="h1">Thanks for checking out this project</h1>
This is something I've been wasting my time on for quite awhile. I started this as something of a curiousity,
then used this data for examining App Ads.txt files. All code for this data scraping, database management
and different frontend dashboards is available on GitHub. If you have any questions, please feel free
to reach out chat.

<TabGroup
	justify="justify-end"
	active="variant-filled-primary"
	hover="hover:variant-soft-primary"
	flex="flex-1 lg:flex-none"
	rounded=""
	border=""
	class="w-full hidden md:inline-flex"
>
	<TabAnchor href="https://ads.jamesoclaire.com/dash/ads">
		<span>Ads.txt Dash</span>
	</TabAnchor>
	<TabAnchor href="https://jamesoclaire.com">
		<span>Blog</span>
	</TabAnchor>
</TabGroup>
<br />
<br />

<h2 class="h2">Github Readme</h2>
{#await fetch(url).then((r) => r.text()) then text}
	{@html marked(text)}
{/await}
