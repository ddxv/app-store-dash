import type { PageServerLoad } from './$types';

export const ssr: boolean = true;
export const csr: boolean = true;

export const load: PageServerLoad = async ({ parent, params }) => {
	const networkName = params.name;
	const res_apps = fetch(`http://localhost:8000/api/companies/${networkName}/topapps`);
	const res_sdks = fetch(`http://localhost:8000/api/companies/${networkName}/sdks`);

	const { companyDetails, companyTree } = await parent();

	const res_parent_categories = fetch(
		`http://localhost:8000/api/companies/${networkName}/parentcategories`
	);
	console.log(`start load overview for company=${networkName}`);
	try {
		return {
			companyDetails: companyDetails,
			companyTree: companyTree,
			companyTopApps: res_apps
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
			companySdks: res_sdks
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company SDKs Not found');
						return 'Company SDKs Not Found';
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
			companyParentCategories: res_parent_categories
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company Parent Categories Not found');
						return 'Company Parent Categories Not Found';
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
