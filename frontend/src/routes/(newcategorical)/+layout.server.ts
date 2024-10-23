import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`load categories start`);

	const res = fetch(`http://localhost:8000/api/categories`);
	const company_types = fetch(`http://localhost:8000/api/companies/types`);

	return {
		appCats: res
			.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 404) {
					console.log('Categories API Not found');
					return 'Categories API Not Found';
				} else if (resp.status === 500) {
					console.log('Categories API Server error');
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
		companyTypes: company_types
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
			)
	};
}
