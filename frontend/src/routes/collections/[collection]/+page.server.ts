export const ssr: boolean = true;
export const csr: boolean = true;

import type { Collection, Collections } from '../../../types.js';

console.log('Script executed');

/** @type {import('../[collection]/$types').PageServerLoad} */
export async function load({ params }): Promise<Collections> {
	const collectionValue = params.collection;
	console.log(`load started collection=${collectionValue}`);
	try {
		const res = await fetch(`http://localhost:8000/api/apps/collections/${collectionValue}`);

		if (!res.ok) {
			const text = await res.text();
			throw new Error(`Failed to fetch collections status ${res.status} ${text}`);
		}

		const app_collections: Collection = await res.json();
		console.log(`loaded collections with len: ${Object.keys(app_collections).length}`);
		return { myapps: app_collections };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
