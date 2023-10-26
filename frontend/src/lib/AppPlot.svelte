<script lang="ts">
	import { ScaleTypes, type LineChartOptions, type ChartTabularData } from '@carbon/charts-svelte';
	import { LineChart } from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	export let plotdata: ChartTabularData;

	export let lineOptions: LineChartOptions = {
		title: 'My Plot Title',
		axes: {
			bottom: {
				title: 'Date',
				mapsTo: 'crawled_date',
				scaleType: ScaleTypes.TIME
			},
			left: {
				mapsTo: 'value',
				// title: 'Installs',
				scaleType: ScaleTypes.LINEAR
			}
		},
		curve: 'curveMonotoneX',
		height: '400px'
	};
	function getPlotOptions(myType: string) {
		return {
			title: myType,
			axes: {
				bottom: {
					title: 'Date',
					mapsTo: 'crawled_date',
					scaleType: ScaleTypes.TIME
				},
				left: {
					mapsTo: 'value',
					scaleType: ScaleTypes.LINEAR
				}
			},
			curve: 'curveMonotoneX',
			height: '400px'
		};
	}
</script>

<div class="card grid grid-cols-1 md:grid-cols-2 gap-4 p-2">
	<LineChart data={plotdata} options={lineOptions} />
</div>
