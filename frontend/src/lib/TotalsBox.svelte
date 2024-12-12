<script lang="ts">
	function formatNumber(num: number) {
		return new Intl.NumberFormat('en-US').format(num);
	}

	let { myTotals, myType } = $props();
</script>

<div class="grid grid-cols-2 gap-4 p-4">
	<div class="stat-container">
		<div class="text-sm text-primary-800-200 uppercase tracking-wide">{myType.name}</div>
		<div class="text-2xl font-bold text-primary-900">
			{formatNumber(myTotals.total_companies)}
		</div>
	</div>

	<div class="stat-container">
		<div class="text-sm text-primary-800-200 uppercase tracking-wide">Total Apps Scanned</div>
		<div class="text-2xl font-bold text-primary-900">
			{formatNumber(myTotals.sdk_total_apps)}
		</div>
	</div>

	<div class="stat-container">
		<div class="text-sm text-primary-800-200 uppercase tracking-wide">Android Apps</div>
		<div class="text-2xl font-bold text-primary-900">
			{formatNumber(myTotals.sdk_android_total_apps)}
		</div>
	</div>

	<div class="stat-container">
		<div class="text-sm text-primary-800-200 uppercase tracking-wide">iOS Apps</div>
		<div class="text-2xl font-bold text-primary-900">
			{formatNumber(myTotals.sdk_ios_total_apps)}
		</div>
	</div>
</div>
