import type { LayoutServerLoad } from './$types';

export const ssr = true;
export const csr = true;

export const load: LayoutServerLoad = async ({ fetch, setHeaders }) => {
	console.log(`load categories start`);
	try {
		const res = await fetch(`http://localhost:8000/api/categories`);

		// Set cache headers
		setHeaders({
			age: res.headers.get('age') || '79000',
			'cache-control': res.headers.get('cache-control') || 'no-store'
		});

		if (res.status === 200) {
			const data = await res.json();
			return { appCats: data };
		} else if (res.status === 404) {
			console.log('Category Not found');
			return { appCats: 'Category Not Found' };
		} else if (res.status === 500) {
			console.log('Categories API Server error');
			return { appCats: 'Backend Error' };
		} else {
			console.log(`Unexpected status: ${res.status}`);
			return { appCats: 'Unexpected Error' };
		}
	} catch (error) {
		console.log('Uncaught error', error);
		return { appCats: 'Uncaught Error' };
	}
};
