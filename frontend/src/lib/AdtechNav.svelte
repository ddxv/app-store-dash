<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	$: urlClassesActive = (href: string) =>
		$page.url.pathname.startsWith(href) ? buttonSelectedColor : '';

	$: paramClassesActive = (pkey: string, pvalue: string) =>
		$page.url.searchParams.get(pkey) == pvalue ? buttonSelectedColor : groupByParents;

	$: paramTimeClassesActive = (pkey: string, pvalue: string) =>
		$page.url.searchParams.get(pkey) == pvalue ? buttonSelectedColor : timeMonth;

	const buttonSelectedColor =
		'radio-item text-base text-center cursor-pointer px-4 py-1 rounded-token variant-filled-primary active:';

	// Function to handle navigation and add or update query params
	function navigateWithParams(path: string, pkey: string, groupBy: string) {
		const url = new URL($page.url.href);
		const groupByParam = url.searchParams.get(pkey) || groupByParents;
		// Override groupBy if a specific value is provided
		if (groupBy) {
			url.searchParams.set(pkey, groupBy);
		}
		goto(`${path}?${url.searchParams.toString()}`);
	}

	const networksURL: string = '/adtech/networks';
	const trackersURL: string = '/adtech/trackers';
	const groupByParents: string = 'parents';
	const groupByBrands: string = 'brands';
	const timeMonth: string = 'month';
	const timeAlltime: string = 'alltime';

	$: currentPath = $page.url.pathname;
</script>

<div class="card">
	<div class="flex">
		<div class="card ml-2 md:ml-4 p-2 md:p-4">
			<h3 class="h5 md:h4 p-2">Time Period</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramTimeClassesActive('time', timeMonth)}
							on:click|preventDefault={() => navigateWithParams(currentPath, 'time', timeMonth)}
						>
							<span class="flex-auto">Most Recent 30 Days</span>
						</a>
					</li>
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramTimeClassesActive('time', timeAlltime)}
							on:click|preventDefault={() => navigateWithParams(currentPath, 'time', timeAlltime)}
						>
							<span class="flex-auto">Alltime</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
		<div class="card mr-2 md:mr-4 p-2 md:p-4">
			<h3 class="h5 md:h4 p-2">Company Category</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="variant-soft-primary">
						<a
							href={networksURL}
							class={urlClassesActive(networksURL)}
							on:click|preventDefault={() => navigateWithParams(networksURL, '', '')}
						>
							<span class="flex-auto">Advertising Networks</span>
						</a>
					</li>
					<li class="variant-soft-primary">
						<a
							href={trackersURL}
							class={urlClassesActive(trackersURL)}
							on:click|preventDefault={() => navigateWithParams(trackersURL, '', '')}
						>
							<span class="flex-auto">Analytics and MMP Attribution Tracking</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>

		<div class="card ml-2 md:ml-4 p-2 md:p-4">
			<h3 class="h5 md:h4 p-2">Granularity</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramClassesActive('groupby', groupByBrands)}
							on:click|preventDefault={() =>
								navigateWithParams(currentPath, 'groupby', groupByBrands)}
						>
							<span class="flex-auto">Group by SubCompany or Brand</span>
						</a>
					</li>
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramClassesActive('groupby', groupByParents)}
							on:click|preventDefault={() =>
								navigateWithParams(currentPath, 'groupby', groupByParents)}
						>
							<span class="flex-auto">Group by Parent Company</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</div>
