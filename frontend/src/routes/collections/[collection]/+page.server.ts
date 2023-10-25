export const ssr: boolean = true;
export const csr: boolean = true;

console.log('Script executed');

interface LoadResponse {
	myapps: any;
	status?: number;
	error?: string;
}

/** @type {import('../[collection]/$types').PageServerLoad} */
export async function load({ params }): Promise<LoadResponse> {
	const collectionValue = params.collection;
	console.log(`load started collection=${collectionValue}`);
	try {
		const res = await fetch(`http://localhost:8000/api/apps/collections/${collectionValue}`);

		if (!res.ok) {
			const text = await res.text();
			throw new Error(`Failed to fetch collections status ${res.status} ${text}`);
		}

		const app_collections: any = await res.json();
		console.log(`loaded collections with len: ${Object.keys(app_collections).length}`);
		return { myapps: app_collections };
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			myapps: {},
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
}
