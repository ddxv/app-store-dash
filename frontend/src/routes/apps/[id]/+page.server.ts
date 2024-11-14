import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, parent }) => {
	const id = params.id;

	const myapp = fetch(`http://localhost:8000/api/apps/${id}`);
	const myranks = fetch(`http://localhost:8000/api/apps/${id}/ranks`);
	const myhistory = fetch(`http://localhost:8000/api/apps/${id}/history`);
	const myPackageInfo = fetch(`http://localhost:8000/api/apps/${id}/packageinfo`);
	const myAdsTxt = fetch(`http://localhost:8000/api/apps/${id}/adstxt`);
	const { appCats } = await parent();
	const { companyTypes } = await parent();

	return {
		myapp: myapp
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
		myranks: myranks
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
		myhistory: myhistory
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
		myPackageInfo: myPackageInfo
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
			),
		myAdsTxt: myAdsTxt
			.then((resp) => {
				if (resp.status === 200) {
					return resp.json();
				} else if (resp.status === 404) {
					console.log('AdsTxt Entries Not found');
					return 'AdsTxt Entries Not Found';
				} else if (resp.status === 500) {
					console.log('AdsTxt Entries API Server error');
					return 'AdsTxt Backend Error';
				}
			})
			.then(
				(json) => json,
				(error) => {
					console.log('Uncaught error', error);
					return 'Uncaught Error';
				}
			),
		appCats: appCats,
		companyTypes: companyTypes
	};
};
