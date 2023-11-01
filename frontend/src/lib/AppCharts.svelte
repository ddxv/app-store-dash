<script lang="ts">
	import { onMount } from 'svelte';
	import * as echarts from 'echarts';

	export let plotData;

	const dimensions = ['crawled_date'];

	// const PyData2 = [
	// 	{
	// 		crawled_date: '2023-10-18',
	// 		'GROSSING: GAME_ROLE_PLAYING': null,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': 48.0
	// 	},
	// 	{
	// 		crawled_date: '2023-10-22',
	// 		'GROSSING: GAME_ROLE_PLAYING': 185.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	},
	// 	{
	// 		crawled_date: '2023-10-23',
	// 		'GROSSING: GAME_ROLE_PLAYING': 170.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	},
	// 	{
	// 		crawled_date: '2023-10-24',
	// 		'GROSSING: GAME_ROLE_PLAYING': 160.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	},
	// 	{
	// 		crawled_date: '2023-10-25',
	// 		'GROSSING: GAME_ROLE_PLAYING': 160.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	},
	// 	{
	// 		crawled_date: '2023-10-26',
	// 		'GROSSING: GAME_ROLE_PLAYING': 159.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	},
	// 	{
	// 		crawled_date: '2023-10-27',
	// 		'GROSSING: GAME_ROLE_PLAYING': 159.0,
	// 		'TOP_FREE: GAME_ROLE_PLAYING': null
	// 	}
	// ];

	const plotSeries = [
		{
			type: 'line',
			symbolSize: 20,
			smooth: true,
			emphasis: {
				focus: 'series'
			},
			lineStyle: {
				width: 4
			}
		},
		{
			type: 'line',
			symbolSize: 20,
			smooth: true,
			emphasis: {
				focus: 'series'
			},

			lineStyle: {
				width: 4
			}
		}
	];

	let myChartDiv: HTMLDivElement;
	let myChart: echarts.ECharts;

	const myDraculaColors = ['#ff79c6', '#bd93f9', '#1ef956', '#f67516'];

	let chartoption = {
		color: myDraculaColors,
		// dataset: PyData,
		dataset: { source: plotData },
		dimensions: dimensions,
		legend: {},
		tooltip: {
			trigger: 'item'
		},
		// grid: {
		// 	left: 30,
		// 	right: 110,
		// 	bottom: 30,
		// 	containLabel: true
		// },
		xAxis: {
			type: 'category',
			splitLine: {
				show: true
			}
			// axisLabel: {
			// 	margin: 30,
			// 	fontSize: 16
			// },
			// boundaryGap: false,
			//data: myX
		},
		yAxis: {
			type: 'value',
			// axisLabel: {
			// 	margin: 34,
			// 	fontSize: 28,
			// 	formatter: '#{value}'
			// },
			inverse: true
			// interval: 1,
			// min: 1,
			// max: 200
		},
		series: plotSeries
	};

	onMount(() => {
		// Create the echarts instance
		myChart = echarts.init(myChartDiv);
		// Draw the chart
		myChart.setOption(chartoption);
		myChart.resize();
	});

	$: if (myChart) {
		// Create the echarts instance
		myChart.dispose();
		myChart = echarts.init(myChartDiv);
		// Draw the chart
		myChart.setOption(chartoption);
		myChart.resize();
	}
</script>

<!-- <svelte:window innerWidth={p} innerHeight={q} /> -->
<div class="w-full h-96" bind:this={myChartDiv} />
