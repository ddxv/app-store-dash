import type { LayoutServerLoad } from './$types';

import { getCachedData } from '../hooks.server';

export const load: LayoutServerLoad = async () => {
	const { appCats, appsOverview, companyTypes } = getCachedData();

	return {
		appCats: appCats,
		appsOverview: appsOverview,
		companyTypes: companyTypes
	};
};
