<script lang="ts">
	import {
		ScaleTypes,
		ComboChart,
		LineChart,
		type ComboChartOptions,
		type ChartTabularData,
		type LineChartOptions
	} from '@carbon/charts-svelte';
	import '@carbon/charts-svelte/styles.css';

	interface Props {
		plotdata: ChartTabularData;
		plotType: string;
		plotHeightPx?: string;
		changeOptions?: ComboChartOptions;
		installOptions?: LineChartOptions;
		numberOptions?: ComboChartOptions;
		appRankOptions?: LineChartOptions;
	}

	let {
		plotdata,
		plotType,
		plotHeightPx = '300px',
		changeOptions = {
			toolbar: { enabled: false },
			axes: {
				bottom: {
					title: 'Date',
					mapsTo: 'crawled_date',
					scaleType: ScaleTypes.TIME
				},
				left: {
					title: 'Rate of Change from Previous Week',
					mapsTo: 'value',
					// percentage: true,
					ticks: {
						formatter: (x: number | Date) => `${x}%`
					},
					scaleType: ScaleTypes.LINEAR,
					correspondingDatasets: ['Rating Rate of Change']
				}
			},
			// curve: 'curveMonotoneX',
			height: '400px',
			comboChartTypes: [
				{
					type: 'grouped-bar',
					correspondingDatasets: [
						'Rating Rate of Change',
						'Installs Rate of Change',
						'Rating Count Rate of Change',
						'Review Count Rate of Change'
					]
					// 	options: {
					// 		points: {
					// 			radius: 5
					// 		}
					// 	}
				}
			]
		},
		installOptions = {
			toolbar: { enabled: false },
			axes: {
				bottom: {
					title: 'Date',
					mapsTo: 'crawled_date',
					scaleType: ScaleTypes.TIME
				},
				left: {
					mapsTo: 'value',
					title: 'Installs',
					scaleType: ScaleTypes.LINEAR,
					correspondingDatasets: ['Installs Daily Average']
				}
			},
			// curve: 'curveMonotoneX',
			height: '400px'
			// comboChartTypes: [
			// 	{
			// 		type: 'grouped-bar',
			// 		correspondingDatasets: ['Installs Daily Average'],
			// 		options: {
			// 			points: {
			// 				radius: 5
			// 			}
			// 		}
			// 	}
			// ]
		},
		numberOptions = {
			toolbar: { enabled: false },
			axes: {
				bottom: {
					title: 'Date',
					mapsTo: 'crawled_date',
					scaleType: ScaleTypes.TIME
				},
				left: {
					mapsTo: 'value',
					title: 'Count',
					scaleType: ScaleTypes.LINEAR,
					correspondingDatasets: ['Installs Daily Average', 'Rating Count Daily Average']
				}
			},
			// curve: 'curveMonotoneX',
			height: '400px',
			comboChartTypes: [
				{
					type: 'stacked-bar',
					correspondingDatasets: [
						'Installs Daily Average',
						'Rating Count Daily Average',
						'Review Count Daily Average'
					],
					options: {
						points: {
							radius: 5
						}
					}
				}
			]
		},
		appRankOptions = {
			title: 'Step (discrete)',
			axes: {
				bottom: {
					title: 'Date',
					mapsTo: 'crawled_date',
					scaleType: ScaleTypes.TIME
				},
				left: {
					mapsTo: 'rank',
					title: 'Conversion rate',
					scaleType: ScaleTypes.LINEAR
				}
			},
			curve: 'curveStepAfter',
			height: plotHeightPx
		}
	}: Props = $props();
</script>

{#if plotType == 'rank'}
	<LineChart data={plotdata} options={appRankOptions} />
{:else if plotType == 'change'}
	<ComboChart data={plotdata} options={changeOptions} />
{:else if plotType == 'number'}
	<ComboChart data={plotdata} options={numberOptions} />
{:else if plotType == 'installs'}
	<LineChart data={plotdata} options={installOptions} />
{:else if plotType == 'ratings'}
	<ComboChart data={plotdata} options={numberOptions} />
{/if}
