import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params }) => {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`search start term=${searchTerm}`);

	return {
		results: fetch(`http://localhost:8000/api/apps/search/${searchTerm}`)
			.then((resp) => {
				if (resp.status === 200) {
					console.log('Search success');
					return resp.json();
				} else if (resp.status === 404) {
					console.log('App Not found');
					return 'App Not Found';
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
};
