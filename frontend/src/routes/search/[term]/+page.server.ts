import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`load started search=${searchTerm}`);
	try {
		const res = fetch(`http://localhost:8000/api/apps/search/${searchTerm}`);
		return { results: { streamed: res.then((resp) => resp.json()) } };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			results: { streamed: {} },
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};

async function fetchSearchResults(term: string) {
	// Your logic to fetch search results goes here.
	// For instance, querying a database or calling another API.
	return [];
}
