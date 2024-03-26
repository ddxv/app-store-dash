import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ parent }) => {
	const { trackers, networks, mycats } = await parent();
	return { trackers, networks, mycats };
};
