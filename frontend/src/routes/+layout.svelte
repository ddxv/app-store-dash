<script>
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-xl uppercase">App Store Data</strong>
			</svelte:fragment>
			<a href="/" class="btn variant-filled">Home</a>
			<a href="/" class="btn variant-filled">Categories?</a>
			<a href="https://ads.jamesoclaire.com" class="btn variant-filled">Ads.txt Dash</a>
			<a href="https://jamesoclaire.com" class="btn variant-filled">Blog</a>
			<a href="/about" class="btn variant-filled">About</a>
			<svelte:fragment slot="trail">
				<a
					class="btn variant-ghost-surface"
					href="https://github.com/ddxv/app-store-dash"
					target="_blank"
					rel="noreferrer">GitHub</a
				>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>

	<!-- Page Route Content -->

	<slot />
</AppShell>
