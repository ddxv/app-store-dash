export const ssr: boolean = true;
export const csr: boolean = true;

import type { LayoutServerLoad } from './$types';

export const load: PageLoad = async ({ fetch, depends, url }) => {
	const emptyResponse = {};

	try {
		const res = await fetch(`http://localhost:8000/api/trackers`);
		const nres = await fetch(`http://localhost:8000/api/networks`);

		return {
			trackers: res.json(),
			networks: nres.json()
		};
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			networks: emptyResponse,
			networksParents: emptyResponse,
			trackers: emptyResponse,
			trackersParents: emptyResponse,
			status: 500,
			error: 'Failed to load adtech ranked apps'
		};
	}
};
