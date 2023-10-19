export const ssr = true;
export const csr = true;
console.log('Script executed');

/** @type {import('../[category]/$types').PageServerLoad} */
export async function load({ params }) {
	console.log('load app started'); try {
		const category = params.category;

		const res = await fetch(`http://localhost:8000/api/categories/${category}`);

		if (!res.ok) {
			throw new Error(`Failed to fetch ${category} with status ${res.status}`);
		}

		const app_detail = await res.json();
		console.log(`loaded app_detail with len: ${Object.keys(app_detail).length}`);
		return { myapp: app_detail };

	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}


