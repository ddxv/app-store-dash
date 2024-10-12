<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<slot name="card1" />
	<slot name="card2" />
	{#if $$slots.card3}
		<!-- This is always true? -->
		<slot name="card3" />
		<div class="col-span-3">
			<slot name="card4" />
		</div>
	{:else}
		<slot name="card4" />
	{/if}
</div>
