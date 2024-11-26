import type { LayoutServerLoad } from './$types';

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

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`root layout load appCats, appsOverview, companyTypes start`);
	const appCats = async () => {
		const resp = await fetch(`http://localhost:8000/api/categories`);
		return checkStatus(resp);
	};
	const appsOverview = async () => {
		const resp = await fetch(`http://localhost:8000/api/apps/overview`);
		return checkStatus(resp);
	};
	const companyTypes = async () => {
		const resp = await fetch(`http://localhost:8000/api/companies/types`);
		return checkStatus(resp);
	};
	console.log(`root layout load appCats, appsOverview, companyTypes end`);

	return {
		appCats: appCats(),
		appsOverview: appsOverview(),
		companyTypes: companyTypes()
	};
};
