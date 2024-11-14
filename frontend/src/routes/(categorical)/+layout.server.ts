import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ parent }) => {
	console.log(`Layout load company types start`);
	const { companyTypes } = await parent();

	return {
		companyTypes: companyTypes
	};
};
