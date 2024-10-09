// import type { PageServerLoad } from '../../$types.js';
import type { PageServerLoad } from './$types.js';

export const ssr: boolean = true;
export const csr: boolean = true;

console.log('Script executed');
export const load: PageServerLoad = async ({ params }) => {
	const networkName = params.name;
	const res = fetch(`http://localhost:8000/api/companies/${networkName}`);
	const res_apps = fetch(`http://localhost:8000/api/companies/${networkName}/apps`);
	const res_tree = fetch(`http://localhost:8000/api/companies/${networkName}/tree`);
	const res_sdks = fetch(`http://localhost:8000/api/companies/${networkName}/sdks`);
	console.log(`start load overview for company=${networkName}`);
	try {
		return {
			companyDetails: res
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
			companyOverview: res_apps
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
			companyTree: res_tree
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('Company Tree Not found');
						return 'Company Tree Not Found';
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
