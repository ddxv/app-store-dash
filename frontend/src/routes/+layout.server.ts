import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`root layout load appCats, appsOverview, companyTypes start`);
	const appCats = await fetch(`http://localhost:8000/api/categories`);
	const appsOverview = await fetch(`http://localhost:8000/api/apps/overview`);
	const companyTypes = await fetch(`http://localhost:8000/api/companies/types`);
	console.log(`root layout load appCats, appsOverview, companyTypes end`);

	return {
		appCats: appCats.status === 200 ? await appCats.json() : 'Layout Categories API Not Found',
		appsOverview:
			appsOverview.status === 200 ? await appsOverview.json() : 'Layout Overview API Not Found',
		companyTypes:
			companyTypes.status === 200 ? await companyTypes.json() : 'Layout Company Types API Not Found'
	};
};
