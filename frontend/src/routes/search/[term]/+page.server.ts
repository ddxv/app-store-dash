import type { RequestHandler } from '@sveltejs/kit';
import type { AppGroup } from '../../../types.js';

import type { SearchResponse } from '../../../types.js';

/** @type {import('../[term]/$types').PageServerLoad} */
export async function load({ params }): Promise<SearchResponse> {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`load started search=${searchTerm}`);
	try {
		const res = await fetch(`http://localhost:8000/api/apps/search/${searchTerm}`);

		if (!res.ok) {
			const text = await res.text();
			throw new Error(`Failed to fetch collections status ${res.status} ${text}`);
		}

		const applications: AppGroup = await res.json();
		console.log(`loaded search results with len: ${Object.keys(applications).length}`);
		return { results: applications };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}

async function fetchSearchResults(term: string) {
	// Your logic to fetch search results goes here.
	// For instance, querying a database or calling another API.
	return [];
}
