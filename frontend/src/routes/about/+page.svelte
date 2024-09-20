<script>
	import discordIcon from '$lib/svg/discord-mark-black.svg?raw';
</script>

<svelte:head>
	<!-- Title -->
	<title>About AppGoblin: Open Source App Analytics | Join Our Community</title>

	<!-- Standard meta tags -->
	<meta
		name="description"
		content="Discover AppGoblin: an open source, self-funded app analytics platform. Learn about our mission, join our community on Discord, and contribute on GitHub to shape the future of app market intelligence."
	/>
	<meta
		name="keywords"
		content="AppGoblin, open source, app analytics, self-funded, community-driven, Discord, GitHub, app market intelligence, mobile app insights"
	/>

	<!-- Open Graph meta tags -->
	<meta property="og:title" content="About AppGoblin: Open Source App Analytics Platform" />
	<meta
		property="og:description"
		content="AppGoblin is a self-funded, open source app analytics platform. Join our community on Discord, contribute on GitHub, and help us revolutionize app market intelligence."
	/>
	<meta property="og:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />
	<meta property="og:url" content="https://appgoblin.info/about" />
	<meta property="og:type" content="website" />

	<!-- Twitter Card meta tags -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta
		name="twitter:title"
		content="About AppGoblin: Open Source App Analytics | Join Our Community"
	/>
	<meta
		name="twitter:description"
		content="Explore AppGoblin: a self-funded, open source platform for app analytics. Learn how you can contribute to our mission of providing comprehensive app market intelligence."
	/>
	<meta name="twitter:image" content="https://appgoblin.info/goblin_purple_hat_250.png" />

	<!-- Additional meta tags -->
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta name="robots" content="index, follow" />
	<link rel="canonical" href="https://appgoblin.info/about" />
</svelte:head>

<div class="p-2 px-8 md:px-32 lg:px-72">
	<h1 class="h1">Thanks for checking out this project</h1>
	<br />
	<div class="card p-2 md:p-8">
		<h3 class="h3 p-2 md:p-4">Background</h3>
		<div class="p-4">
			<p>
				Originally this came out of a curiosity I had about the IAB app-ads.txt standard in 2022. In
				order to scrape app-ads.txt files I had to first get 4,000,000+ iOS and Android apps + their
				respective publisher URLs. While that project, like app-ads.txt itself, went unused, I
				remained interested in letting the database of apps keep growing. Then in the fall of 2023
				while on haitus from real work, I started working on an API and UI.
			</p>
			<br />
			<p>
				Now, App Goblin is the combination of several open source projects I built. Yes, there are a
				large number of similar companies like data.ai and sensortower.com which have many more
				features. But it was a great project for me to learn more frontend and javascript as well as
				give me something to do with the scraper which I had built previously (whats the point of a
				database if you cant use it somehow). For now App Goblin is simply here as a resource free
				of charge as it's running costs only $20 a month or so in hosting.
			</p>
			<br />
			<p>If you have questions or suggestions please feel free to reach out.</p>
			<a href="https://jamesoclaire.com">
				<h2>
					<span>jamesoclaire.com</span>
				</h2>
			</a>
		</div>
	</div>
	<br />

	<div class="card p-2 md:p-8">
		<h3 class="h3 p-2 md:p-4">Marketing Community & Feedback</h3>
		<div class="p-4">
			<p>
				I'm happy to help brainstorm if you're looking to do marketing or advertising for iOS or
				Android. Additionally, I'd love to keep working on features for Android and iOS app
				marketers. Feel free to join my AppGoblin Discord channel to chat ideas.
			</p>
			<a
				class="btn btn-sm variant-ghost-surface"
				href="https://discord.gg/7jpWEhkXRW"
				target="_blank"
				rel="noreferrer"
			>
				<p>Chat on Discord</p>
				<div class="inline-flex items-center">
					{@html discordIcon}
				</div>
			</a>
			<br />
			<br />
			<br />
			You can also reach me personally:
			<a href="https://jamesoclaire.com">
				<p>https://jamesoclaire.com</p>
			</a>
		</div>
	</div>
	<br />

	<div class="card p-2 md:p-4">
		<h3 class="h3 p-2 md:p-4">Open Source Tech Stack</h3>
		<div class="p-2 md:p-4">
			<p>
				First is the underlying data which is collected and maintained from <strong
					><a href="https://github.com/ddxv/adscrawler">github.com/ddxv/adscrawler</a></strong
				>
				The adscrawler uses Python & PostgreSQL to crawl app stores to collect apps and their basic information
				like names and rating counts. This data is then stored to the PostgreSQL database.
			</p>
			<br />
			<p>
				The website itself is also open source and can be found at
				<strong
					><a href="https://github.com/ddxv/app-store-dash">github.com/ddxv/app-store-dash</a
					></strong
				> The website is built from a Python backend API based on LiteStar which manages queries to the
				PostgreSQL database. The API is used by a JavaScript Svelte frontend with Tailwind and Skeleton
				for CSS. All projects are glued together with systemd and websockets where needed. Everything
				is hosted on AWS in the small EC2 instances.
			</p>
		</div>
	</div>
</div>
