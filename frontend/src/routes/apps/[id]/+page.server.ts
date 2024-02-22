export const ssr = true;
export const csr = true;

import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, setHeaders, locals }) => {
	const emptyResponse = { streamed: 'Caught error!' };
	const id = params.id;

	// setHeaders({
	// 	'cache-control': 'max-age=40000'
	// });

	const res = fetch(`http://localhost:8000/api/apps/${id}`);

	const ranks = fetch(`http://localhost:8000/api/apps/${id}/ranks`);

	const appHistory = fetch(`http://localhost:8000/api/apps/${id}/history`);

	const packageInfo = fetch(`http://localhost:8000/api/apps/${id}/packageinfo`);

	try {
		return {
			myapp: {
				streamed: res
					.then((resp) => {
						if (resp.status === 200) {
							return resp.json();
						} else if (resp.status === 404) {
							console.log('App Not found');
							return 'App Not Found';
						} else if (resp.status === 500) {
							console.log('App API Server error');
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
			},
			myranks: {
				streamed: ranks
					.then((resp) => {
						if (resp.status === 200) {
							return resp.json();
						} else if (resp.status === 404) {
							console.log('App Ranks Not found');
							return 'App Not Found';
						} else if (resp.status === 500) {
							console.log('Ranks API Server error');
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
			},
			myhistory: {
				streamed: appHistory
					.then((resp) => {
						if (resp.status === 200) {
							return resp.json();
						} else if (resp.status === 404) {
							console.log('App History Not found');
							return 'App Not Found';
						} else if (resp.status === 500) {
							console.log('App History API Server error');
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
			},
			myPackageInfo: {
				streamed: packageInfo
					.then((resp) => {
						if (resp.status === 200) {
							return resp.json();
						} else if (resp.status === 404) {
							console.log('App Ranks Not found');
							return 'App Not Found';
						} else if (resp.status === 500) {
							console.log('Ranks API Server error');
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
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			myapp: emptyResponse,
			myranks: emptyResponse,
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};
