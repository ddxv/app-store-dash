export const ssr: boolean = true;
export const csr: boolean = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, setHeaders, url }) => {
	const emptyResponse = {};
	setHeaders({
		'cache-control': 'max-age=3600'
	});
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
			ranks: res.then((resp) => resp.json()),
			history: history.then((resp) => resp.json())
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
