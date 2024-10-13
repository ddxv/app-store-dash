import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch }) => {
	console.log(`load categories start`);
	try {
		const res = await fetch(`http://localhost:8000/api/categories`);

		if (res.status === 200) {
			const data = await res.json();
			return { mycats: data };
		} else if (res.status === 404) {
			console.log('Category Not found');
			return { mycats: 'Category Not Found' };
		} else if (res.status === 500) {
			console.log('Categories API Server error');
			return { mycats: 'Backend Error' };
		} else {
			console.log(`Unexpected status: ${res.status}`);
			return { mycats: 'Unexpected Error' };
		}
	} catch (error) {
		console.log('Uncaught error', error);
		return { mycats: 'Uncaught Error' };
	}
};
