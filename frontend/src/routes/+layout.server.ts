import type { LayoutServerLoad } from './$types';

// Create a simple cache store
let cache = {
	appCats: null,
	appsOverview: null,
	companyTypes: null,
	lastFetched: 0
};

// Cache duration (e.g., 24 hours in milliseconds)
const CACHE_DURATION = 24 * 60 * 60 * 1000;

export const load: LayoutServerLoad = async ({ fetch }) => {
	// Check if cache is valid
	if (
		cache.appCats &&
		cache.appsOverview &&
		cache.companyTypes &&
		Date.now() - cache.lastFetched < CACHE_DURATION
	) {
		return {
			appCats: cache.appCats,
			appsOverview: cache.appsOverview,
			companyTypes: cache.companyTypes
		};
	}

	// If cache is invalid or empty, fetch new data
	try {
		const [appCats, appsOverview, companyTypes] = await Promise.all([
			fetch(`http://localhost:8000/api/categories`).then((res) => res.json()),
			fetch(`http://localhost:8000/api/apps/overview`).then((res) => res.json()),
			fetch(`http://localhost:8000/api/companies/types`).then((res) => res.json())
		]);

		// Update cache
		cache = {
			appCats,
			appsOverview,
			companyTypes,
			lastFetched: Date.now()
		};

		return {
			appCats,
			appsOverview,
			companyTypes
		};
	} catch (error) {
		console.error('Error loading data:', error);
		return {
			appCats: [],
			appsOverview: [],
			companyTypes: []
		};
	}
};
