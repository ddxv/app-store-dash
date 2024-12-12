// import type { PageServerLoad } from '../../$types.js';
import type { PageServerLoad } from './$types.js';

export const ssr: boolean = true;
export const csr: boolean = true;

export const load: PageServerLoad = async ({ params, parent }) => {
	console.log(`start load overview for companies in ${params.category}`);
	const res = fetch(`http://localhost:8000/api/companies/categories/${params.category}`);

	const { appCats } = await parent();

	try {
		return {
			companiesOverview: res
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
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
				),
			appCats: await appCats
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
