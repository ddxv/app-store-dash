import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`search start term=${searchTerm}`);

	const appsResponse = fetch(`http://localhost:8000/api/apps/search/${searchTerm}`);
	const companiesResponse = fetch(`http://localhost:8000/api/companies/search/${searchTerm}`);

	try {
		return {
			results: appsResponse
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company Not found');
						return 'Company Not Found';
					} else if (resp.status === 500) {
						console.log('API Server error');
						return 'Backend Error';
					}
				})
				.then(
					(json) => json,
					(error) => {
						console.log('Uncaught error', error);
						return 'Uncaught Error';
					}
				),
			companiesResults: companiesResponse
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company Not found');
						return 'Company Not Found';
					} else if (resp.status === 500) {
						console.log('API Server error');
						return 'Backend Error';
					}
				})
				.then(
					(json) => json,
					(error) => {
						console.log('Uncaught error', error);
						return 'Uncaught Error';
					}
				)
		};
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			results: {},
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};
