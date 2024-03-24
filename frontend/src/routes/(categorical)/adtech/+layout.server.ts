export const ssr: boolean = true;
export const csr: boolean = true;

import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
	const emptyResponse = {};

	try {
		const res = fetch(`http://localhost:8000/api/trackers`);
		const nres = fetch(`http://localhost:8000/api/networks`);

		return {
			trackers: res.then((resp) => resp.json()),
			networks: nres.then((resp) => resp.json())
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
