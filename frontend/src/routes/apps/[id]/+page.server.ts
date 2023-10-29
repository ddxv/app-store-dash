export const ssr = true;
export const csr = true;

import type { AppFullDetails } from '../../../types.js';

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	// export async function load({ params }): Promise<PageServerData> {
	console.log('load app started');
	try {
		const id = params.id;

		const res = await fetch(`http://localhost:8000/api/apps/${id}`);
		const ranks = await fetch(`http://localhost:8000/api/apps/${id}/ranks`);

		if (!res.ok) {
			throw new Error(`Failed to fetch ${id} with status ${res.status}`);
		}

		const app_detail = await res.json();
		const rank_details = await ranks.json();
		console.log(`loaded app_detail with len: ${Object.keys(app_detail).length}`);
		return {
			myapp: app_detail,
			myranks: rank_details
		}
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
