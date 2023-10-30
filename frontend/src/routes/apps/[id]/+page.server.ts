export const ssr = true;
export const csr = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	console.log('load app started');
	try {
		const id = params.id;

		const res = await fetch(`http://localhost:8000/api/apps/${id}`);

		if (!res.ok) {
			throw new Error(`Failed to fetch app ${id} with status ${res.status}`);
		}

		const app_detail = await res.json();
		console.log(`loaded app_detail with len: ${Object.keys(app_detail).length}`);

		let rank_details = {};

		try {
			const ranks = await fetch(`http://localhost:8000/api/apps/${id}/ranks`);
			if (!ranks.ok) {
				console.warn(`Failed to fetch ranks for app ${id} with status ${ranks.status}`);
			} else {
				rank_details = await ranks.json();
			}
		} catch (rankError) {
			console.warn('Failed to fetch ranks:', rankError);
		}

		return {
			myapp: app_detail,
			myranks: rank_details
		};
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};
