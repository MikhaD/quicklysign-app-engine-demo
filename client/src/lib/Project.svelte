<script lang="ts">
	export let title: string;
	export let link: string;
	export let image: string;
	export let description: string;
	export let points: string[] = [];
</script>

<div class="project">
	<img src={image} alt="" />
	<h4><a href={link} about="_blank">{title}</a></h4>
	<div class="description">{description}</div>
	<div class="body">
		{#if points.length > 0}
			<ul>
				{#each points as point}
					<li>{point}</li>
				{/each}
			</ul>
		{/if}
	</div>
</div>

<style lang="scss">
	.project {
		display: grid;
		grid-template-columns: 1fr 6fr;
		grid-template-rows: auto auto auto;
		column-gap: 1rem;
	}
	img {
		grid-row-start: 1;
		grid-row-end: 4;
		border-radius: 1rem;
		aspect-ratio: 1;
		width: 100%;
	}
	h4 {
		margin-block: 0 1.5rem;
	}
	a {
		color: var(--fg-00);
	}
	ul {
		padding-left: 2rem;
	}

	@media (width < 50rem) {
		.project {
			grid-template-columns: 1fr 4fr;
			grid-template-rows: 3rem auto auto;
		}
		img {
			grid-row-start: 1;
			grid-row-end: 3;
		}
		.body {
			grid-column-start: 1;
			grid-column-end: 3;
		}
	}
</style>
