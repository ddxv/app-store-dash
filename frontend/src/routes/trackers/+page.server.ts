export const ssr: boolean = true;
export const csr: boolean = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ setHeaders }) => {
	const emptyResponse = { streamed: {} };
	setHeaders({
		'cache-control': 'max-age=3600'
	});
	try {
		const res = fetch(`http://localhost:8000/api/trackers`);

		return {
			companies: {
				streamed: res.then((resp) => resp.json())
			}
		};
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			ranks: emptyResponse,
			history: emptyResponse,
			status: 500,
			error: 'Failed to load ranked apps'
		};
	}
};
