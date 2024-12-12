import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`search start term=${searchTerm}`);

	try {
		const response = await fetch(`http://localhost:8000/api/apps/search/${searchTerm}/playstore`);
		if (response.status === 200) {
			console.log('Search success');
			return { results: await response.json() };
		} else if (response.status === 404) {
			console.log('SearchTerm Not found');
			return { results: 'SearchTerm Not Found' };
		} else if (response.status === 500) {
			console.log('API Server error');
			return { results: 'Backend Error' };
		}
	} catch (error) {
		console.log('Uncaught error', error);
		return { results: 'Uncaught Error' };
	}
};
