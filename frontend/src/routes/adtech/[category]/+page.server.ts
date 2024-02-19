import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ parent }) => {
	const { trackers, networks } = await parent();
	return { trackers, networks };
};
