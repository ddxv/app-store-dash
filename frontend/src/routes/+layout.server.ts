import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`layout load categories start`);
	const appCats = await fetch(`http://localhost:8000/api/categories`);
	const appsOverview = await fetch(`http://localhost:8000/api/apps/overview`);

	return {
		appCats: appCats.status === 200 ? appCats.json() : 'Layout Categories API Not Found',
		appsOverview:
			appsOverview.status === 200 ? appsOverview.json() : 'Layout Overview API Not Found'
	};
};
