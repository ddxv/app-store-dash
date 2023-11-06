<script lang="ts">
	import { onMount } from 'svelte';
	import * as echarts from 'echarts';

	export let plotData;

	export let maxValue: number | null = null;

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

	// const plotSeries = [
	// 	{
	// 		type: 'line',
	// 		symbolSize: 20,
	// 		smooth: true,
	// 		emphasis: {
	// 			focus: 'series'
	// 		},
	// 		lineStyle: {
	// 			width: 4
	// 		}
	// 	},
	// 	{
	// 		type: 'line',
	// 		symbolSize: 20,
	// 		smooth: true,
	// 		emphasis: {
	// 			focus: 'series'
	// 		},

	// 		lineStyle: {
	// 			width: 4
	// 		}
	// 	}
	// ];

	const defaultSeries = {
		type: 'line',
		symbolSize: 20,
		smooth: true,
		emphasis: {
			focus: 'series'
		},
		lineStyle: {
			width: 4
		},
		endLabel: { show: true, formatter: '{a}', distance: 20, valueAnimation: true }
	};

	function makeSeries(plotData: Object[]) {
		const numberOfSeries = Object.keys(plotData[plotData.length - 1]).length - 1;
		const myArray = [];
		for (let i = 0; i < numberOfSeries; i++) {
			myArray.push(defaultSeries);
		}
		return myArray;
	}

	const plotSeries = makeSeries(plotData);

	let myChartDiv: HTMLDivElement;
	let myChart: echarts.ECharts;

	const myColors = [
		'#636efa',
		'#EF553B',
		'#00cc96',
		'#ab63fa',
		'#FFA15A',
		'#19d3f3',
		'#FF6692',
		'#B6E880',
		'#FF97FF',
		'#FECB52',
		'#AA0DFE',
		'#3283FE',
		'#85660D',
		'#782AB6',
		'#565656',
		'#1C8356',
		'#16FF32',
		'#F7E1A0',
		'#E2E2E2',
		'#1CBE4F',
		'#C4451C',
		'#DEA0FD',
		'#FE00FA',
		'#325A9B',
		'#FEAF16',
		'#F8A19F',
		'#90AD1C',
		'#F6222E',
		'#1CFFCE',
		'#2ED9FF',
		'#B10DA1',
		'#C075A6',
		'#FC1CBF',
		'#B00068',
		'#FBE426',
		'#FA0087'
	];

	let chartoption = {
		color: myColors,
		dataset: { source: plotData },
		dimensions: dimensions,
		grid: {
			x: 40, //left
			y: 10, // top
			x2: 55, // right
			y2: 30 // bottom
			// containLabel: true
		},
		// legend: {},
		tooltip: {
			trigger: 'item'
		},
		xAxis: {
			type: 'category',
			splitLine: {
				show: true
			},
			axisLabel: {
				margin: 10,
				fontSize: 18
			}
			// boundaryGap: false,
			//data: myX
		},
		yAxis: {
			type: 'value',
			axisLabel: {
				margin: 10,
				fontSize: 22,
				formatter: '#{value}'
			},
			inverse: true,
			// interval: 1,
			// min: 1,
			max: maxValue
		},
		series: plotSeries
	};

	onMount(() => {
		// Create the echarts instance
		myChart = echarts.init(myChartDiv);
		// Draw the chart
		myChart.setOption(chartoption);
		myChart.resize();

		const myfun = () => {
			myChart.resize();
		};

		window.addEventListener('resize', myfun);

		return () => {
			window.removeEventListener('resize', myfun);
		};
	});

	$: if (myChart) {
		// Create the echarts instance
		myChart.dispose();
		// myChart = echarts.init(myChartDiv, null, { renderer: 'svg' });
		myChart = echarts.init(myChartDiv);
		// Draw the chart
		myChart.setOption(chartoption);
		myChart.resize();
	}
</script>

<div class="w-full h-96" bind:this={myChartDiv} />
