<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	const buttonSelectedColor =
		'radio-item text-base text-center cursor-pointer px-4 py-1 rounded-token variant-filled-primary active:';

	// Function to handle navigation and add or update query params
	function navigateWithParams(path: string, pkey: string, groupBy: string) {
		const url = new URL($page.url.href);
		// Override groupBy if a specific value is provided
		if (groupBy) {
			url.searchParams.set(pkey, groupBy);
		}
		goto(`${path}?${url.searchParams.toString()}`);
	}

	const groupByParents: string = 'parents';
	const groupByBrands: string = 'brands';
	const metricInstalls: string = 'installs';
	const metricAppCount: string = 'appcount';

	let paramClassesActive = $derived((pkey: string, pvalue: string) =>
		$page.url.searchParams.get(pkey) == pvalue ? buttonSelectedColor : groupByParents
	);
	let paramMetricClassesActive = $derived((pkey: string, pvalue: string) =>
		$page.url.searchParams.get(pkey) == pvalue ? buttonSelectedColor : metricInstalls
	);
	let currentPath = $derived($page.url.pathname);
</script>

<div class="card">
	<div class="flex">
		<div class="card ml-2 md:ml-4 p-2 md:p-4">
			<h3 class="h5 md:h4 p-2">Metric</h3>
			<nav class="list-nav">
				<ul class="rounded-md variant-outline-primary">
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramMetricClassesActive('metric', metricInstalls)}
							onclick={(event) => {
								navigateWithParams(currentPath, 'metric', metricInstalls);
								event.preventDefault();
							}}
						>
							<span class="flex-auto">Installs Past 30 Days</span>
						</a>
					</li>
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramMetricClassesActive('metric', metricAppCount)}
							onclick={(event) => {
								navigateWithParams(currentPath, 'metric', metricAppCount);
								event.preventDefault();
							}}
						>
							<span class="flex-auto">Count of Apps</span>
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
							onclick={(event) => {
								navigateWithParams(currentPath, 'groupby', groupByBrands);
								event.preventDefault();
							}}
						>
							<span class="flex-auto">Group by SubCompany or Brand</span>
						</a>
					</li>
					<li class="variant-soft-primary">
						<a
							href={currentPath}
							class={paramClassesActive('groupby', groupByParents)}
							onclick={(event) => {
								navigateWithParams(currentPath, 'groupby', groupByParents);
								event.preventDefault();
							}}
						>
							<span class="flex-auto">Group by Parent Company</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</div>
