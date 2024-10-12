import type { LayoutServerLoad } from './../../$types';

export const load: LayoutServerLoad = async ({ params }) => {
	const networkName = params.name;

	const res = fetch(`http://localhost:8000/api/companies/${networkName}`);

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
			)
	};
};