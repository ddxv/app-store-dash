export const ssr: boolean = true;
export const csr: boolean = false;

import type { AppGroup, DeveloperResponse } from '../../../types.js';

console.log('Script executed');

/** @type {import('../[developer]/$types').PageServerLoad} */
export async function load({ params }): Promise<DeveloperResponse> {
	const developerValue = params.developer;
	console.log(`load started collection=${developerValue}`);
	try {
		const res = await fetch(`http://localhost:8000/api/apps/developers/${developerValue}`);

		if (!res.ok) {
			const text = await res.text();
			throw new Error(`Failed to fetch developers status ${res.status} ${text}`);
		}

		const app_collections: AppGroup = await res.json();
		console.log(`loaded developers with len: ${Object.keys(app_collections).length}`);
		return { results: app_collections };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
