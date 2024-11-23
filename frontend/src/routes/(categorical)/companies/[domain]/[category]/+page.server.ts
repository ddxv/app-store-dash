import type { PageServerLoad } from './$types.js';

export const ssr: boolean = true;
export const csr: boolean = true;

export const load: PageServerLoad = async ({ parent, params }) => {
	const companyDomain = params.domain;
	const category = params.category;
	const res_apps = fetch(
		`http://localhost:8000/api/companies/${companyDomain}/topapps?category=${category}`
	);

	const { companyDetails, companyTree } = await parent();

	console.log(`start load overview for company=${companyDomain}`);
	try {
		return {
			companyDetails: companyDetails,
			companyTree: companyTree,
			companyCategoryApps: res_apps
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company + Category Not found');
						return 'Company + Category Not Found';
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
