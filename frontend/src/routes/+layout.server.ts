import type { PageServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: PageServerLoad = async () => {
	// console.log(`load categories start`);
	const res = fetch(`http://localhost:8000/api/categories`);

	// setHeaders({
	// 	'cache-control': 'max-age=40000'
	// });

	return {
		mycats: {
			streamed: res
				.then((resp) => {
					if (resp.status === 200) {
						return resp.json();
					} else if (resp.status === 404) {
						console.log('App Not found');
						return 'App Not Found';
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
				)
		}
	};
};
