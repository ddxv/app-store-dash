<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	let data = [20, 100, 50, 12, 20, 130, 45];
	let labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

	// const mylabels = Utils.months({ count: 7 });
	// const mydata = {
	// 	labels: labels,
	// 	datasets: [
	// 		{
	// 			label: 'My First Dataset',
	// 			data: [65, 59, 80, 81, 56, 55, 40],
	// 			fill: false,
	// 			borderColor: 'rgb(75, 192, 192)',
	// 			tension: 0.1
	// 		}
	// 	]
	// };

	//WORKING FOR EXAMPLE LINE
	let ctx;
	let canvas;
	let myRed = 'rgb(255, 99, 132)';
	let myoptions = {
		options: {
			interaction: {
				mode: 'nearest',
				intersect: true
			},
			events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove']
		},
		type: 'line',
		data: {
			labels: labels,
			datasets: [
				{
					label: 'Unit Sales',
					data: data,
					borderWidth: 5,
					hoverBackgroundColor: myRed,
					hoverBorderJoinStyle: 'round',
					tension: 0.3,
					// fill: true,
					pointBackgroundColor: myRed,
					backgroundColor: myRed,
					borderColor: myRed,
					pointStyle: 'circle',
					pointRadius: 10,
					pointHoverRadius: 15
				}
			]
		}
	};

	var OGoptions = {
		type: 'line',
		data: {
			labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
			datasets: [
				{
					label: '# of Votes',
					data: [12, 19, 3, 5, 2, 3],
					backgroundColor: '#FF0000',
					borderWidth: 5,
					borderColor: '#FF0000'
				},
				{
					label: '# of Points',
					data: [7, 11, 5, 8, 3, 7],
					backgroundColor: '#0000FF',
					borderWidth: 5,
					borderColor: '#0000FF'
				},
				{
					label: '# of Cars',
					data: [18, 4, 12, 6, 9, 2],
					backgroundColor: '#FF1493',
					borderWidth: 5,
					borderColor: '#FF1493'
				}
			]
		},
		options: {
			onHover: (e, activeEls, chart) => {
				if (activeEls.length === 0) {
					chart.data.datasets.forEach((dataset) => {
						dataset.borderWidth = dataset.borderWidth == 15 ? 5 : dataset.borderWidth;
						dataset.backgroundColor =
							dataset.backgroundColor.length === 9
								? dataset.backgroundColor.slice(0, -2)
								: dataset.backgroundColor;
						dataset.borderColor =
							dataset.borderColor.length === 9
								? dataset.borderColor.slice(0, -2)
								: dataset.borderColor;
					});
					chart.update();
					return;
				}
				const hoveredEl = chart.getElementsAtEventForMode(
					e,
					'point',
					{
						intersect: false,
						axis: 'x'
					},
					true
				)[0];
				chart.data.datasets.forEach((dataset, i) => {
					dataset.borderWidth =
						hoveredEl.datasetIndex === i || dataset.borderWidth.length == 5
							? 15
							: dataset.borderWidth;
					dataset.backgroundColor =
						hoveredEl.datasetIndex === i || dataset.backgroundColor.length === 9
							? dataset.backgroundColor
							: dataset.backgroundColor + '4D';
					dataset.borderColor =
						hoveredEl.datasetIndex === i || dataset.borderColor.length === 9
							? dataset.borderColor
							: dataset.borderColor + '4D';
				});
				chart.update();
			}
		}
	};

	const hoverlineoptions = {
		type: 'line',
		data: {
			labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
			datasets: [
				{
					label: '# of Votes',
					data: [12, 19, 3, 5, 2, 3],
					backgroundColor: '#FF0000',
					borderWidth: 4,
					borderColor: '#FF0000'
				},
				{
					label: '# of Points',
					data: [7, 11, 5, 8, 3, 7],
					backgroundColor: '#0000FF',
					borderWidth: 4,
					borderColor: '#0000FF'
				},
				{
					label: '# of Cars',
					data: [18, 4, 12, 6, 9, 2],
					backgroundColor: '#FF1493',
					borderWidth: 4,
					borderColor: '#FF1493'
				}
			]
		},
		options: {
			responsive: true,
			interaction: {
				intersect: false,
				mode: 'nearest'
			},
			events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
			onLeave: (event, chart) => {
				chart.data.datasets.forEach((dataset) => {
					dataset.borderWidth = 4;
				});
			},
			onHover: (event, chartElement, chart) => {
				if (chartElement.length > 0) {
					const firstPoint = chartElement[0];
					// Check if the hovered element is a line
					if (firstPoint && firstPoint.datasetIndex !== undefined) {
						const elements = chart.getElementsAtEventForMode(
							event,
							'nearest',
							{ intersect: false },
							true
						);
						// If there are elements (i.e., the line), apply custom animation or effects
						if (elements.length > 0) {
							console.log('Hovering over the line!');

							chart.data.datasets.forEach((dataset, i) => {
								if (elements[0].datasetIndex === i) {
									dataset.borderWidth = 15; // Highlight the hovered dataset
								} else {
									dataset.borderWidth = 5; // Reset other datasets
								}
							});
						}
					}
				} else {
					// If not hovering over any dataset, reset all datasets
					chart.data.datasets.forEach((dataset) => {
						dataset.borderWidth = 4;
					});
				}
				chart.update({
					duration: 150,
					easing: 'easeOutBounce'
				});
			}
		}
	};

	// onMount(() => {
	// 	ctx = canvas.getContext('2d');
	// 	var chart = new Chart(ctx, options);
	// });

	onMount(() => {
		ctx = canvas.getContext('2d');
		var chart = new Chart(ctx, hoverlineoptions);
		// var chart = new Chart(ctx, hoverlineoptions);
	});
</script>

<canvas bind:this={canvas} />
