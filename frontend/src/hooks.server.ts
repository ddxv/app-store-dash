import type { Handle } from '@sveltejs/kit';
import type { ServerInit } from '@sveltejs/kit';

let appCats: any[] = [];
let appsOverview: any = {};
let companyTypes: any[] = [];

export const init: ServerInit = async () => {
	[appCats, appsOverview, companyTypes] = await Promise.all([
		fetch(`http://localhost:8000/api/categories`).then((res) => res.json()),
		fetch(`http://localhost:8000/api/apps/overview`).then((res) => res.json()),
		fetch(`http://localhost:8000/api/companies/types`).then((res) => res.json())
	]);
	console.log('Data initialized on server start');
};

export const getCachedData = () => ({
	appCats,
	appsOverview,
	companyTypes
});

export const handle: Handle = async ({ event, resolve }) => {
	const route = event.url.pathname;

	if (route.startsWith('/networks')) {
		return new Response(undefined, {
			status: 301,
			headers: { Location: '/companies/types/ad-networks' }
		});
	}
	if (route.startsWith('/trackers')) {
		return new Response(undefined, {
			status: 301,
			headers: { Location: '/companies/types/ad-attribution' }
		});
	}
	if (route.startsWith('/adtech')) {
		return new Response(undefined, { status: 301, headers: { Location: '/companies' } });
	}
	if (route.startsWith('/companies/types/monetization')) {
		return new Response(undefined, {
			status: 301,
			headers: { Location: '/companies/types/ad-networks' }
		});
	}

	// let start = performance.now();
	const response = await resolve(event);
	// let end = performance.now();
	// let duration = end - start;
	// duration = duration.toFixed(2);
	// console.log(`${route} took ${duration}ms`);

	return response;
};
