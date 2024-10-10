<script lang="ts">
	import { DonutChart, type DonutChartOptions, type ChartTabularData } from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	export let plotData: ChartTabularData;
	// export let plotType: string;
	export let plotHeightPx: string = '300px';

	export let categoryPieOptions: DonutChartOptions = {
		title: 'Apps by Category',
		resizable: true,
		donut: {
			center: {
				label: 'Apps'
			}
		},
		height: plotHeightPx
	};

	// const plotData = [
	// 	{ group: 'education', value: 29288 },
	// 	{ group: 'music_and_audio', value: 26783 },
	// 	{ group: 'tools', value: 22139 },
	// 	{ group: 'books_and_reference', value: 21724 },
	// 	{ group: 'personalization', value: 20852 },
	// 	{ group: 'entertainment', value: 18725 },
	// 	{ group: 'game_puzzle', value: 17417 },
	// 	{ group: 'game_casual', value: 15402 }
	// ];
</script>

<DonutChart data={plotData} options={categoryPieOptions} />
