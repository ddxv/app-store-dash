import type { PageServerLoad } from './$types.js';

function checkStatus(resp: Response, name: string) {
	if (resp.status === 200) {
		return resp.json();
	} else if (resp.status === 404) {
		console.log(`App ${name} Not found`);
		return `${name} Not Found`;
	} else if (resp.status === 500) {
		console.log(`App ${name} API Server error`);
		return `${name} API Server error`;
	} else {
		throw new Error('Unknown error');
	}
}

export const load: PageServerLoad = async ({ params, parent }) => {
	const id = params.id;
	// Load parent data first because it is cached
	const { appCats, companyTypes } = await parent();

	const myapp = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}`);
		return checkStatus(resp, 'App');
	};

	const myranks = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/ranks`);
		return checkStatus(resp, 'App Ranks');
	};
	const myhistory = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/history`);
		return checkStatus(resp, 'App History');
	};
	const myPackageInfo = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/packageinfo`);
		return checkStatus(resp, 'App Package Info');
	};
	const myAdsTxt = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/${id}/adstxt`);
		return checkStatus(resp, 'App AdsTxt');
	};

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
