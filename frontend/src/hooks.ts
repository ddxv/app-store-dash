import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	if (event.url.pathname === '/networks') {
		return new Response(undefined, { status: 301, headers: { Location: '/adtech/networks' } });
	}
	if (event.url.pathname === '/trackers') {
		return new Response(undefined, { status: 301, headers: { Location: '/adtech/trackers' } });
	}

	// For all other paths, proceed with the request as usual
	const response = await resolve(event);
	return response;
};
