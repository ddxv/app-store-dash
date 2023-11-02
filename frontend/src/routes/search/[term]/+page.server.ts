import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, locals }) => {
	const term = params.term;
	const searchTerm = decodeURIComponent(term);
	console.log(`load started search=${searchTerm}`);

	const res = fetch(`http://localhost:8000/api/apps/search/${searchTerm}`);
	return {
		results: {
			streamed: res
				.then((resp) => {
					if (resp.status === 200) {
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
		}
	};
};
