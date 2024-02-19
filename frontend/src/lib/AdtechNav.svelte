<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	$: urlClassesActive = (href: string) =>
		$page.url.pathname.startsWith(href) ? buttonSelectedColor : '';

	$: paramClassesActive = (pkey: string, pvalue: string) =>
		$page.url.searchParams.get(pkey) == pvalue ? buttonSelectedColor : groupByParents;

	const buttonSelectedColor =
		'radio-item text-base text-center cursor-pointer px-4 py-1 rounded-token variant-filled-primary active:';

	// Function to handle navigation and add or update query params
	function navigateWithParams(path: string, groupBy: string) {
		const url = new URL($page.url.href);
		const groupByParam = url.searchParams.get('groupby') || groupByParents;
		// Override groupBy if a specific value is provided
		if (groupBy) {
			url.searchParams.set('groupby', groupBy);
		}
		goto(`${path}?${url.searchParams.toString()}`);
	}

	const networksURL: string = '/adtech/networks';
	const trackersURL: string = '/adtech/trackers';
	const groupByParents: string = 'parents';
	const groupByBrands: string = 'brands';

	$: currentPath = $page.url.pathname;
</script>

<div class="card mx-4 p-4">
	<div class="flex">
		<div class="card mx-4 p-4">
			<h3 class="h5 md:h4 p-2">Company Category</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="flex variant-soft-primary p-1">
						<a
							href={networksURL}
							class={urlClassesActive(networksURL)}
							on:click|preventDefault={() => navigateWithParams(networksURL, '')}
						>
							<span class="flex-auto">Advertising Networks</span>
						</a>
						<a
							href={trackersURL}
							class={urlClassesActive(trackersURL)}
							on:click|preventDefault={() => navigateWithParams(trackersURL, '')}
						>
							<span class="flex-auto">Analytics and MMP Attribution Tracking</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
		<div class="card mx-4 p-4">
			<h3 class="h5 md:h4 p-2">Granularity</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="flex variant-soft-primary p-1">
						<a
							href={currentPath}
							class={paramClassesActive('groupby', groupByBrands)}
							on:click|preventDefault={() => navigateWithParams(currentPath, groupByBrands)}
						>
							<span class="flex-auto">Group by SubCompany or Brand</span>
						</a>
						<a
							href={currentPath}
							class={paramClassesActive('groupby', groupByParents)}
							on:click|preventDefault={() => navigateWithParams(currentPath, groupByParents)}
						>
							<span class="flex-auto">Group by Parent Company</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</div>
