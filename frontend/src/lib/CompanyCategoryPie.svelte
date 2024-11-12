<script lang="ts">
	import { DonutChart, type DonutChartOptions, type ChartTabularData } from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	interface Props {
		plotData: ChartTabularData;
		// export let plotType: string;
		plotHeightPx?: string;
		categoryPieOptions?: DonutChartOptions;
	}

	let {
		plotData,
		plotHeightPx = '300px',
		categoryPieOptions = {
			title: 'Apps by Category',
			theme: 'g90',
			resizable: true,
			donut: {
				center: {
					label: 'Apps'
				}
			},
			height: plotHeightPx
		}
	}: Props = $props();

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

<div class="p-4">
	<DonutChart data={plotData} options={categoryPieOptions} />
</div>
