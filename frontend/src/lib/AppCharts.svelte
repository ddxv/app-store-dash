<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	//WORKING FOR EXAMPLE LINE
	let ctx;
	let canvas;
	const myDraculaColors = ['#ff79c6', '#bd93f9', '#1ef956', '#f67516'];

	const hoverlineoptions = {
		type: 'line',
		data: {
			labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
			datasets: [
				{
					label: '# of Votes',
					yAxisID: 'y1',
					data: [1, 1, 2, 3, 6, 8],
					backgroundColor: myDraculaColors[0],
					borderWidth: 4,
					borderColor: myDraculaColors[0],
					tension: 0.5,
					pointRadius: 5,
					pointHitRadius: 5
				},
				{
					label: '# of Points',
					yAxisID: 'y1',
					data: [2, 4, 4, 5, 3, 5],
					backgroundColor: myDraculaColors[1],
					borderWidth: 4,
					borderColor: myDraculaColors[1],
					tension: 0.5,
					pointRadius: 5,
					pointHitRadius: 5
				},
				{
					label: '# of Cars',
					yAxisID: 'y1',
					data: [5, 6, 7, 6, 5, 4],
					backgroundColor: myDraculaColors[2],
					borderWidth: 4,
					borderColor: myDraculaColors[2],
					tension: 0.5,
					pointRadius: 5,
					pointHitRadius: 5
				}
			]
		},
		options: {
			scales: { y1: { reverse: true, type: 'linear', display: true, position: 'left' } },
			responsive: true,
			interaction: {
				intersect: false,
				mode: 'nearest'
			},
			// events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
			onLeave: (event, chartElement, chart) => {
				chart.data.datasets.forEach((dataset) => {
					dataset.borderWidth = 4;
				});
			},
			onHover: (event, chartElement, chart) => {
				// If there are elements (i.e., the line), apply custom animation or effects
				console.log('Hovering over the line!');

				chart.data.datasets.forEach((dataset, i) => {
					if (chartElement[0].datasetIndex === i) {
						dataset.borderWidth = 8; // Highlight the hovered dataset
						dataset.pointRadius = 8; // Highlight the hovered dataset
					} else {
						dataset.borderWidth = 4; // Reset other datasets
						dataset.pointRadius = 5; // Highlight the hovered dataset
					}
				});
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
