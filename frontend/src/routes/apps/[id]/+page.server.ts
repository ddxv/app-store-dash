import type { PageServerLoad } from './$types.js';

function checkStatus(resp: Response) {
	if (resp.status === 200) {
		return resp.json();
	} else if (resp.status === 404) {
		console.log('App Not found');
		return 'App Not Found';
	} else if (resp.status === 500) {
		console.log('App API Server error');
		return 'Backend Error';
	} else {
		throw new Error('Unknown error');
	}
}

export const load: PageServerLoad = async ({ params, parent }) => {
	const id = params.id;

	const myapp = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}`);
		return checkStatus(resp);
	};

	const myranks = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/ranks`);
		return checkStatus(resp);
	};
	const myhistory = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/history`);
		return checkStatus(resp);
	};
	const myPackageInfo = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/packageinfo`);
		return checkStatus(resp);
	};
	const myAdsTxt = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/adstxt`);
		return checkStatus(resp);
	};

	// Load parent data first because it is cached
	const { appCats, companyTypes } = await parent();

	return {
		myapp: myapp(),
		myranks: myranks(),
		myhistory: myhistory(),
		myPackageInfo: myPackageInfo(),
		myAdsTxt: myAdsTxt(),
		appCats: appCats,
		companyTypes: companyTypes
	};
};
