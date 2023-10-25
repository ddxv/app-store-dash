export const ssr = true;
export const csr = true;

/** @type {import('../[id]/$types').PageServerLoad} */
export async function load({ params }) {
	console.log('load app started');
	try {
		const id = params.id;

		const res = await fetch(`http://localhost:8000/api/apps/${id}`);

		if (!res.ok) {
			throw new Error(`Failed to fetch ${id} with status ${res.status}`);
		}

		const app_detail = await res.json();
		console.log(`loaded app_detail with len: ${Object.keys(app_detail).length}`);
		return { myapp: app_detail };
	} catch (error) {
		console.error('Failed to load app data:', error);
		return {
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
