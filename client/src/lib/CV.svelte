<script lang="ts">
	import Job from "./Job.svelte";
	import Project from "./Project.svelte";
	import Skill from "./Skill.svelte";

	async function fetchDatapoints(url: string, count: number) {
		return await (await fetch(`${url}?count=${count}`)).json();
	}

	const skills = fetchDatapoints("/api/skills", 14);
	const projects = fetchDatapoints("/api/projects", 6);
	const jobs = fetchDatapoints("/api/jobs", 5);
</script>

<div class="cv">
	<h2>Junior Software Developer CV</h2>
	<h3>Technical Skills</h3>
	<hr />
	<p>Skills are listed in order of how long they have been actively used.</p>
	<div class="skills">
		{#await skills}
			<p>Loading...</p>
		{:then skills}
			{#each skills as skill}
				<Skill icon={skill.icon} skill={skill.skill} years={skill.years} />
			{/each}
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
	<h3>Professional Experience</h3>
	<hr />
	<div class="jobs">
		{#await jobs}
			<p>Loading...</p>
		{:then jobs}
			{#each jobs as job}
				<Job
					employer={job.employer}
					title={job.title}
					start={job.start}
					end={job.end}
					location={job.location}
					points={job.points}
				/>
			{/each}
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
	<h3>Education</h3>
	<hr />
	<div>
		<h4>2019 - 2023 Major in Computer Science, University of Cape Town</h4>
		<ul>
			<li>
				Received a <a
					href="https://github.com/MikhaD/MikhaD/blob/main/images/certificate_of_merit.png"
					target="_blank">certificate of merit</a
				> for exceptional performance in Computer Science CSC3003S.
			</li>
			<li>Received A grades for all graded computer science courses.</li>
		</ul>
	</div>
	<div>
		<h4>2018 NSC, Matric, Michael Oak Waldorf School, Cape Town.</h4>
		<ul>
			<li>
				Achieved 5 distinctions including Mathematics, Physical Sciences, English, and
				Computer Applications Technology.
			</li>
			<li>Class representative for 3 years, Co-Chair of the student council for 1.</li>
			<li>Captain of the school's Ultimate Frisbee team.</li>
		</ul>
	</div>
	<h3>Projects</h3>
	<hr />
	<p>
		A more comprehensive list of personal projects can be found at
		<a href="https://mikha.dev" target="_blank">mikha.dev</a>.
	</p>
	<div class="projects">
		{#await projects}
			<p>Loading...</p>
		{:then projects}
			{#each projects as project}
				<Project
					title={project.title}
					link={project.link}
					image={project.image}
					description={project.description}
					points={project.points}
				/>
			{/each}
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
	<h3>References</h3>
	<hr />
	<p>References available on request.</p>
</div>

<style lang="scss">
	.cv {
		--padding: 2.5rem;
		max-width: calc(var(--page-width) + 2 * var(--padding));
		margin-inline: auto;
		padding-inline: 2.5rem;
		font-family: var(--font-mono);
	}
	.skills {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(25rem, 1fr));
		column-gap: 15%;
	}
	h2,
	h3,
	hr {
		color: var(--accent);
	}

	h2 {
		font-size: 2em;
		text-align: center;
		margin-block: 3rem;
	}
	h3 {
		font-size: 1.5em;
	}

	a {
		color: var(--fg-00);
	}
</style>
