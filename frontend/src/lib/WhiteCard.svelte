<div class="card bg-white rounded-lg overflow-hidden">
	{#if $$slots.title}
		<div class="card-header text-2xl bg-surface-50 border-b border-gray-200">
			<slot name="title" />
		</div>
	{/if}
	<div class="card-content">
		<slot />
	</div>
</div>
