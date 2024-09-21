import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params }) => {
	const id = params.id;

	return {
		myapp: fetch(`http://localhost:8000/api/apps/${id}`)
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
			),
		myranks: fetch(`http://localhost:8000/api/apps/${id}/ranks`)
			.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 404) {
					console.log('App Ranks Not found');
					return 'App Not Found';
				} else if (resp.status === 500) {
					console.log('App Ranks API Server error');
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
		myhistory: fetch(`http://localhost:8000/api/apps/${id}/history`)
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
			),
		myPackageInfo: fetch(`http://localhost:8000/api/apps/${id}/packageinfo`)
			.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 404) {
					console.log('Package Info Not found');
					return 'Package Info Not Found';
				} else if (resp.status === 500) {
					console.log('Package Info API Server error');
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
