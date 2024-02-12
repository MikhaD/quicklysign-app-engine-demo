<script lang="ts">
	export let icon: string;
	export let skill: string;
	export let years: number;

	function timeText(years: number) {
		if (years < 1) return `${Math.round(12 * years)} months`;
		if (years == 1) return "year";
		return "years";
	}
</script>

<div>
	<img src="https://raw.githubusercontent.com/MikhaD/MikhaD/main/icons/{icon}" alt={skill} />
	<span class="skill">{skill}</span>
	<span class="time">({years} {timeText(years)})</span>
</div>

<style lang="scss">
	div {
		display: flex;
		gap: 1rem;
		height: 2.5rem;
		align-items: center;
		&:hover {
			background-color: var(--bg-02);
		}
	}
	.time {
		/* background-color: #fff; */
		flex: 1;
		text-align: right;
	}
	img {
		display: inline-block;
		height: 60%;
		aspect-ratio: 1;
	}
	.skill {
		text-transform: capitalize;
	}
</style>
