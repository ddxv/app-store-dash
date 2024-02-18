import type { PageServerLoad } from './$types.js';

export const ssr: boolean = true;
export const csr: boolean = true;

console.log('Script executed');
export const load: PageServerLoad = async ({ params, locals }) => {
	const trackerName = params.name;
	const res = fetch(`http://localhost:8000/api/companies/${trackerName}`);
	console.log(`start load apps for tracker=${trackerName}`);
	try {
		return {
			results: {
				streamed: res
					.then((resp) => {
						if (resp.status === 200) {
							return resp.json();
						} else if (resp.status === 404) {
							console.log('Tracker Not found');
							return 'Tracker Not Found';
						} else if (resp.status === 500) {
							console.log('API Server error');
							return 'Backend Error';
						}
					})
					.then(
						(json) => json,
						(error) => {
							console.log('Uncaught error', error);
							return 'Uncaught Error';
						}
					)
			}
		};
	} catch (error) {
		console.error('Failed to load data:', error);
		return {
			results: { streamed: {} },
			status: 500,
			error: 'Failed to load trending apps'
		};
	}
};
