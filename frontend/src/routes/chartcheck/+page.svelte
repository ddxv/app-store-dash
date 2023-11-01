<script lang="ts">
	import RankEChart from '$lib/RankEChart.svelte';
	import AppCharts from '$lib/AppCharts.svelte';
</script>

<div class="grid grid-cols-2 gap-4 p-8 bg-primary-100">
	<div class="card variant-glass-surface">
		<AppCharts />
	</div>
	<div class="card variant-glass-surface">
		<RankEChart />
	</div>
</div>
