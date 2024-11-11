<script lang="ts">
	import {
		BarChartSimple,
		ScaleTypes,
		type ChartTabularData,
		type BarChartOptions
	} from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	interface Props {
		plotData: ChartTabularData;
		plotTitle: string;
		plotHeightPx?: string;
		chartOptions?: BarChartOptions;
	}

	let {
		plotData,
		plotTitle,
		plotHeightPx = '300px',
		chartOptions = {
			title: plotTitle,
			theme: 'g90', // <- how to set the theme
			axes: {
				left: {
					mapsTo: 'group',
					scaleType: ScaleTypes.LABELS
				},
				bottom: {
					mapsTo: 'value'
				}
			},
			height: plotHeightPx
		}
	}: Props = $props();

	// export let plotData: ChartTabularData = [
	//   {
	//     group: 'Qty',
	//     value: 65000
	//   },
	//   {
	//     group: 'More',
	//     value: 29123
	//   },
	//   {
	//     group: 'Sold',
	//     value: 35213
	//   },
	//   {
	//     group: 'Restocking',
	//     value: 51213
	//   },
	//   {
	//     group: 'Misc',
	//     value: 16932
	//   }
	// ]
</script>

<div class="p-4">
	<BarChartSimple data={plotData} options={chartOptions} />
</div>
