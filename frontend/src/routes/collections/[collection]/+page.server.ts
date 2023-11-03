export const ssr: boolean = true;
export const csr: boolean = true;

import type { PageServerLoad } from './$types.js';

import type { Collection, Collections } from '../../../types.js';

export const load: PageServerLoad = async ({ params, setHeaders, locals }) => {
	const collectionValue = params.collection;
	console.log(`load started collection=${collectionValue}`);
	setHeaders({ 'cache-control': 'max-age=40000' });
	const res = fetch(`http://localhost:8000/api/apps/collections/${collectionValue}`);
	return {
		AppCollections: {
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
