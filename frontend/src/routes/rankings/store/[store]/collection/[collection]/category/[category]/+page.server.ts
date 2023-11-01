export const ssr: boolean = true;
export const csr: boolean = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, url }) => {
	const emptyResponse = { streamed: {} };
	try {
		const storeVal = params.store;
		const collectionValue = params.collection;
		const categoryValue = params.category;
		const res = fetch(
			`http://localhost:8000/api/rankings/${storeVal}/${collectionValue}/${categoryValue}`
		);
		const history = fetch(
			`http://localhost:8000/api/rankings/${storeVal}/${collectionValue}/${categoryValue}/history`
		);

		return {
			ranks: {
				streamed: res.then((resp) => resp.json())
			},
			history: {
				streamed: history.then((resp) => resp.json())
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
