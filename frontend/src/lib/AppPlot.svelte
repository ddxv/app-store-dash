<script lang="ts">
	import {
		ScaleTypes,
		ComboChart,
		type ComboChartOptions,
		type ChartTabularData
	} from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	export let plotdata: ChartTabularData;

	export let lineOptions: ComboChartOptions = {
		title: 'Recent Ratings, Installs and Review Counts',
		axes: {
			bottom: {
				title: 'Date',
				mapsTo: 'crawled_date',
				scaleType: ScaleTypes.TIME
			},
			left: {
				mapsTo: 'installs_avg_per_day',
				title: 'Avg Installs per Day',
				scaleType: ScaleTypes.LINEAR,
				correspondingDatasets: ['installs_avg_per_day']
			},
			right: {
				mapsTo: 'rating_count_avg_per_day',
				title: 'Rating Avg',
				scaleType: ScaleTypes.LINEAR,
				correspondingDatasets: ['rating_count_avg_per_day']
			}
		},
		// curve: 'curveMonotoneX',
		height: '400px',
		comboChartTypes: [
			{
				type: 'simple-bar',
				correspondingDatasets: ['installs_avg_per_day']
			},
			{
				type: 'line',
				options: {
					points: {
						radius: 5
					}
				},
				correspondingDatasets: ['rating_count_avg_per_day']
			}
		]
	};
</script>

<ComboChart data={plotdata} options={lineOptions} />
