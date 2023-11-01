<script>
	import { onMount } from 'svelte';

	// const theme = skeleton.getThemeProperties('skeleton');
	// const bgColor = theme['--color-primary-500'];

	import * as echarts from 'echarts';

	let myChartDiv, myChart;

	const myDraculaColors = ['#ff79c6', '#bd93f9', '#1ef956', '#f67516'];

	const years = ['2001', '2002', '2003', '2004', '2005', '2006'];

	let chartoption = {
		color: myDraculaColors,
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
			},
			// axisLabel: {
			// 	margin: 30,
			// 	fontSize: 16
			// },
			// boundaryGap: false,
			data: years
		},
		yAxis: {
			type: 'value',
			// axisLabel: {
			// 	margin: 34,
			// 	fontSize: 28,
			// 	formatter: '#{value}'
			// },
			inverse: true,
			interval: 1,
			min: 1,
			max: 8
		},
		series: [
			{
				name: '# of Votes',
				data: [1, 1, 2, 3, 6, 8],
				type: 'line',
				symbolSize: 20,
				smooth: true,
				emphasis: {
					focus: 'series'
				},
				endLabel: {
					show: true,
					formatter: '{a}',
					distance: 18,
					fontSize: 20
				},
				lineStyle: {
					width: 4
				}
			},
			{
				name: '# of Points',
				type: 'line',
				data: [2, 4, 4, 5, 3, 5],
				symbolSize: 20,
				smooth: true,
				emphasis: {
					focus: 'series'
				},
				endLabel: {
					show: true,
					formatter: '{a}',
					distance: 18,
					fontSize: 20
				},
				lineStyle: {
					width: 4
				}
			},
			{
				name: '# of Cars',
				type: 'line',
				data: [5, 6, 7, 6, 5, 4],
				symbolSize: 20,
				smooth: true,
				emphasis: {
					focus: 'series'
				},
				endLabel: {
					show: true,
					formatter: '{a}',
					distance: 20
				},
				lineStyle: {
					width: 4
				}
			}
		]
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

<!-- <canvas bind:this={canvas} /> -->

<!-- <svelte:window innerWidth={p} innerHeight={q} /> -->
<!-- <div id="echartsRank" style="width: 600px;height:400px;" /> -->
<div class="w-full h-96" bind:this={myChartDiv} />
