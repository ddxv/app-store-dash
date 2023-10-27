export const ssr = true;
export const csr = true;

import type { CategoriesInfo, MyCats } from '../types';

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<CategoriesInfo> {
	console.log(`load categories start`);
	try {
		const res = await fetch(`http://localhost:8000/api/categories`);

		if (!res.ok) {
			throw new Error(`Failed to fetch categories with status ${res.status}`);
		}

		const categories: MyCats = await res.json();

		console.log(`load categories len: ${Object.keys(categories).length}`);
		return { mycats: categories };
	} catch (error) {
		console.error('Failed to load layout categories data:', error);
		return {
			mycats: { categories: {} },
			status: 500,
			error: 'Failed to load categories'
		};
	}
}
