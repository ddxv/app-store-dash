export const ssr: boolean = true;
export const csr: boolean = true;

import type { Collection, Collections } from '../../types.js';

console.log('Script executed');

export async function load({ params, url }) {
	let lang = url.searchParams.get('lang');
	let store = url.searchParams.get('store');
	let collection = url.searchParams.get('collection');
	return { lang, store, collection };
}

// /** @type {import('../[collection]/$types').PageServerLoad} */
// export async function load({ params }) {
// 	// console.log(`load started collection=${collectionValue}`);
// 	// try {
// 	// 	const res = await fetch(`http://localhost:8000/api/apps/rankings/${storeValue}/${collectionValue}/${categoryValue}`);

// 	// 	if (!res.ok) {
// 	// 		const text = await res.text();
// 	// 		throw new Error(`Failed to fetch collections status ${res.status} ${text}`);
// 	// 	}

// 	// 	const app_collections: Collection = await res.json();
// 	// 	console.log(`loaded collections with len: ${Object.keys(app_collections).length}`);
// 	// 	return { myapps: app_collections };
// 	// } catch (error) {
// 	// 	console.error('Failed to load data:', error);
// 	// 	return {
// 	// 		status: 500,
// 	// 		error: 'Failed to load trending apps'
// 	// 	};
// 	// }
// }
