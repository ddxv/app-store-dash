export const ssr: boolean = true;
export const csr: boolean = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, setHeaders, url }) => {
	const emptyResponse = {};
	setHeaders({
		'cache-control': 'max-age=3600'
	});
	try {
		const androidAppRanks = fetch(`http://localhost:8000/api/rankings/1/1/1/short`);
		const iOSAppRanks = fetch(`http://localhost:8000/api/rankings/2/4/120/short`);

		const androidGameRanks = fetch(`http://localhost:8000/api/rankings/1/1/36/short`);
		const iOSGameRanks = fetch(`http://localhost:8000/api/rankings/2/4/62/short`);

		return {
			androidAppRanks: androidAppRanks.then((resp) => resp.json()),
			iOSAppRanks: iOSAppRanks.then((resp) => resp.json()),
			androidGameRanks: androidGameRanks.then((resp) => resp.json()),
			iOSGameRanks: iOSGameRanks.then((resp) => resp.json())
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
