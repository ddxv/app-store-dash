import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`layout load categories start`);
	const res = await fetch(`http://localhost:8000/api/categories`);
	const appsOverview = await fetch(`http://localhost:8000/api/apps/overview`);

	return {
		appCats: res.status === 200 ? res.json() : 'Category Not Found',
		appsOverview: appsOverview.status === 200 ? appsOverview.json() : 'Overview Not Found'
	};
};
