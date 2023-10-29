export const ssr: boolean = true;
export const csr: boolean = true;

console.log('Script executed');

export async function load({ params, url }) {
	let lang = url.searchParams.get('lang');
	let store = url.searchParams.get('store');
	let collection = url.searchParams.get('collection');
	return { lang, store, collection };
}
