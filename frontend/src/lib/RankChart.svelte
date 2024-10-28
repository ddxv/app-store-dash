<script lang="ts">
	import { run } from 'svelte/legacy';

	import { onMount } from 'svelte';
	import * as echarts from 'echarts';

	import { plotColors } from '../stores';

	let myInterval;
	let topPadding;
	let rightPadding;

	interface Props {
		plotData: any;
		maxValue?: number | undefined;
		narrowBool?: boolean;
	}

	let { plotData, maxValue = undefined, narrowBool = false }: Props = $props();

	const dimensions = ['crawled_date'];

	if (maxValue && maxValue <= 10) {
		myInterval = 1;
	} else {
		myInterval = undefined;
	}

	const defaultSeries: echarts.SeriesOption = {
		type: 'line',
		symbolSize: 20,
		smooth: true,
		emphasis: {
			focus: 'series'
		},
		lineStyle: {
			width: 4
		}
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

	let myChartDiv: HTMLDivElement = $state();
	let myChart: echarts.ECharts = $state();
	if (narrowBool) {
		// Legend at top!
		topPadding = 40;
		rightPadding = 20;
	} else {
		// No Legend at top, at right
		topPadding = 20;
		rightPadding = 55;
	}

	let gridoption: echarts.GridComponentOption = {
		left: 50,
		top: topPadding,
		right: rightPadding,
		bottom: 40
		// containLabel: true
	};

	let chartoption: echarts.EChartsOption = $state({
		color: plotColors,
		dataset: { source: plotData },
		dimensions: dimensions,
		grid: gridoption,
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
			min: 1,
			interval: myInterval,
			max: maxValue
		},
		series: plotSeries
	});

	if (narrowBool) {
		// Legend at top!
		chartoption['legend'] = {};
	} else {
		// No Legend at top, at right
		defaultSeries['endLabel'] = {
			show: true,
			formatter: '{a}',
			distance: 20,
			valueAnimation: true
		};
	}

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

	run(() => {
		if (myChart) {
			// Create the echarts instance
			myChart.dispose();
			// myChart = echarts.init(myChartDiv, null, { renderer: 'svg' });
			myChart = echarts.init(myChartDiv);
			// Draw the chart
			myChart.setOption(chartoption);
			myChart.resize();
		}
	});
</script>

<div class="w-full h-96" bind:this={myChartDiv}></div>
