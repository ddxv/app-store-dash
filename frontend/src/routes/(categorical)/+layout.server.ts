import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ parent }) => {
	const { companyTypes } = await parent();

	return {
		companyTypes: companyTypes
	};
};
