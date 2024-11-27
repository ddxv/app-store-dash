import type { PageServerLoad } from './$types.js';
export const prerender = 'auto';

export const load: PageServerLoad = async ({}) => {
	const res = fetch(`http://localhost:8000/api/companies`);
	console.log(`start load overview for companies`);
	try {
		return {
			companiesOverview: res
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 406) {
						console.log('Companes overview not found');
						return 'Company overview not Found';
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
