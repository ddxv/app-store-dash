import { join } from 'path';
import type { Config } from 'tailwindcss';

import { skeleton } from '@skeletonlabs/skeleton/plugin';
import * as themes from '@skeletonlabs/skeleton/themes';

const config = {
	// darkMode: 'selector',
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		join(require.resolve('@skeletonlabs/skeleton-svelte'), '../**/*.{html,js,svelte,ts}')
	],
	theme: {
		extend: {}
	},
	plugins: [
		skeleton({
			themes: [themes.nouveau, themes.catppuccin]
		})
	]
} satisfies Config;

export default config;
