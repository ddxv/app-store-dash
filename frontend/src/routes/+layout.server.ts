import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`root layout load appCats, appsOverview, companyTypes start`);
	const [appCats, appsOverview, companyTypes] = await Promise.all([
		fetch(`http://localhost:8000/api/categories`).then((res) => res.json()),
		fetch(`http://localhost:8000/api/apps/overview`).then((res) => res.json()),
		fetch(`http://localhost:8000/api/companies/types`).then((res) => res.json())
	]);

	console.log(`root layout load appCats, appsOverview, companyTypes end`);

	return {
		appCats: appCats,
		appsOverview: appsOverview,
		companyTypes: companyTypes
	};
};
