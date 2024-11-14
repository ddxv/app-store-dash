import type { PageServerLoad } from './$types.js';

export const ssr: boolean = true;
export const csr: boolean = true;

export const load: PageServerLoad = async ({ params }) => {
	const value_pattern = params.pattern;

	const res = fetch(`http://localhost:8000/api/sdks/${value_pattern}`);
	const res_companies = fetch(`http://localhost:8000/api/sdks/${value_pattern}/companies`);

	console.log(`start load overview for sdks for ${value_pattern}`);
	try {
		return {
			matchedCompanies: res_companies.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 500) {
					console.log('API Server error');
					return 'Backend Error';
				}
			}),
			matchedApps: res
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 406) {
						console.log(`Sdk for ${value_pattern} not found`);
						return 'Sdk for pattern not Found';
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
			error: 'Failed to load sdks'
		};
	}
};
