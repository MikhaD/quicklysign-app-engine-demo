<script lang="ts">
	import Job from "./Job.svelte";
	import Project from "./Project.svelte";
	import Skill from "./Skill.svelte";
</script>

<div class="cv">
	<h2>Junior Software Developer CV</h2>
	<h3>Technical Skills</h3>
	<hr />
	<p>Skills are listed in order of how long they have been actively used.</p>
	<div class="skills">
		<Skill icon="python.svg" skill="python" time="5 years" />
		<Skill icon="html-dark.svg" skill="HTML" time="5 years" />
		<Skill icon="css-dark.svg" skill="CSS" time="5 years" />
		<Skill icon="javascript.svg" skill="JavaScript" time="4 years" />
		<Skill icon="git.svg" skill="git" time="4 years" />
		<Skill icon="vscode.svg" skill="VS Code" time="4 years" />
		<Skill icon="figma.svg" skill="Figma" time="4 years" />
		<Skill icon="java.svg" skill="java" time="4 years" />
		<Skill icon="typescript.svg" skill="TypeScript" time="3 years" />
		<Skill icon="scss.svg" skill="SCSS" time="3 years" />
		<Skill icon="linux.svg" skill="linux" time="2 years" />
		<Skill icon="svelte.svg" skill="svelte" time="2 years" />
		<Skill icon="github_actions.svg" skill="github actions" time="2 years" />
		<Skill icon="node.svg" skill="NodeJS" time="1 years" />
	</div>
	<h3>Professional Experience</h3>
	<hr />
	<div class="jobs">
		<Job
			employer="University of Cape Town"
			location="Cape Town South Africa"
			title="Senior Computer Science Tutor"
			start="02/2022"
			end="10/2023"
			points={[
				"Ran the Computer Science (CS) hotseat for 6 - 9 hours per week.",
				"Taught CS concepts to hundreds of students, in groups and individually.",
				"Learned to quickly spot errors and debug code over people's shoulders.",
				"Increased student's marks to the point many became tutors themselves.",
			]}
		></Job>
	</div>
	<h3>Education</h3>
	<hr />
	<div>
		<h4>2019 - 2023 Major in Computer Science, University of Cape Town</h4>
		<ul>
			<li>
				Received a <a
					href="https://github.com/MikhaD/MikhaD/blob/main/images/certificate_of_merit.png"
					about="_blank">certificate of merit</a
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
		<a href="https://mikha.dev" about="_blank">mikha.dev</a>.
	</p>
	<div class="projects">
		<Project
			title="Wordle+"
			link="https://mikhad.github.io/wordle/"
			description="A recreation of the original wordle game written in Svelte using Typescript
			with additional modes and features such as word definitions and infinite mode."
			image="https://mikhad.github.io/wordle/img/logo_192x192.png"
			points={[
				"Over 2 200 000 page views in 2023 alone from 140 countries.",
				"Number one google search result for wordle infinite and wordle plus.",
				"Received over 150 stars on GitHub and 170 forks.",
				"Dealt with over 50 issues and pull requests.",
			]}
		/>
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
