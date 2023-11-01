export const ssr = true;
export const csr = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	console.log('load app started');
	const emptyResponse = { streamed: {} };
	try {
		const id = params.id;

		const res = fetch(`http://localhost:8000/api/apps/${id}`);

		const ranks = fetch(`http://localhost:8000/api/apps/${id}/ranks`);

		return {
			myapp: {
				streamed: res.then((resp) => resp.json())
			},
			myranks: {
				streamed: ranks.then((resp) => resp.json())
			}
		};
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			myapp: emptyResponse,
			myranks: emptyResponse,
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};
