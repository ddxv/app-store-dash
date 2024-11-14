export const ssr: boolean = true;
export const csr: boolean = true;

import type { Category, CategoryResponse } from '../../../types.js';

/** @type {import('../[category]/$types').PageServerLoad} */
export async function load({ params }): Promise<CategoryResponse> {
	const category = params.category;
	console.log(`load started collection=${category}`);
	try {
		const res = await fetch(`http://localhost:8000/api/categories/${category}`);

		if (!res.ok) {
			const text = await res.text();
			throw new Error(`Failed to fetch collections status ${res.status} ${text}`);
		}

		const app_collections: Category = await res.json();
		console.log(`loaded categories with len: ${Object.keys(app_collections).length}`);
		return { results: app_collections };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
