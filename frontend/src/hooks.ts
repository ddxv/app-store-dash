import type { Handle } from '@sveltejs/kit';

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

	let start = performance.now();

	// For all other paths, proceed with the request as usual
	const response = await resolve(event);
	let end = performance.now();

	let duration = end - start;
	duration = duration.toFixed(2);

	console.log(`${route} took ${duration}ms`);
	return response;
};
