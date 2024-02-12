<script lang="ts">
	export let title: string;
	export let start: string;
	export let end = "present";
	export let employer: string;
	export let location: string;
	export let points: string[] = [];
</script>

<div>
	<h4>{title} - {employer}</h4>
	<div>
		{#if start == end}
			{start},
		{:else}
			{start} - {end},
		{/if}
		{location}
	</div>
	{#if points.length > 0}
		<ul>
			{#each points as point}
				<li>{point}</li>
			{/each}
		</ul>
	{/if}
</div>

<style>
	h4 {
		margin-bottom: 0.5rem;
	}
</style>
