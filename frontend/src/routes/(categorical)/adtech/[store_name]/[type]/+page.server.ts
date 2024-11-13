import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ parent, depends, url }) => {
	depends(`page:${url.searchParams}`);

	const { trackers, networks, appCats } = await parent();
	return { trackers, networks, appCats };
};
