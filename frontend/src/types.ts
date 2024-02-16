import type { ChartTabularData } from '@carbon/charts-svelte';

export interface AppGroup {
	apps: AppFullDetail[];
	title: string;
}

export interface Category {
	key: string;
	google: AppGroup;
	ios: AppGroup;
}

export interface CategoryResponse {
	results?: Category;
	status?: number;
	error?: string;
}

export interface DeveloperResponse {
	results: { streamed: AppGroup };
	status?: number;
	error?: string;
}

export interface TrackerApps {
	results: { streamed: AppGroup };
	status?: number;
	error?: string;
}
export interface SearchResponse {
	results: { streamed: AppGroup };
	status?: number;
	error?: string;
}

export interface Collection {
	categories: AppGroup;
	title: string;
}

export interface Collections {
	AppCollections: { streamed: Collection };
	status?: number;
	error?: string;
}

export interface CategoryInfo {
	id: string;
	name: string;
	android: string;
	ios: string;
}

export interface CatData {
	categories: Record<string, CategoryInfo>;
}

export interface CategoriesInfo {
	mycats: { streamed: Promise<CatData> };
	status?: number;
	error?: string;
}
export interface AppRankResponse {
	myranks?: AppRankDetail;
	status?: number;
	error?: string;
}

export interface HomeData {
	androidAppRanks: {
		streamed: Promise<{ ranks: RankedApps[] }>;
	};
	iOSAppRanks: {
		streamed: Promise<{ ranks: RankedApps[] }>;
	};
	androidGameRanks: {
		streamed: Promise<{ ranks: RankedApps[] }>;
	};
	iOSGameRanks: {
		streamed: Promise<{ ranks: RankedApps[] }>;
	};
	status?: number;
	error?: string;
	// history: {
	// 	streamed: Promise<{ history: RankedApps[] }>;
	// };
}

export interface RankedAppList {
	ranks: RankedApps[];
}

export interface StoreCategoryRanks {
	ranks: {
		streamed: Promise<{ ranks: RankedApps[] }>;
	};
	status?: number;
	error?: string;
	history: {
		streamed: Promise<{ history: RankedApps[] }>;
	};
}

export interface RankedApps {
	rank: number;
	name: string;
	store_id: string;
	icon_url_512: string;
}
export interface AppRankDetail {
	crawled_date: string;
	rank: number;
	store: number;
	collection: string;
	category: string;
}

interface Networks {
	[key: string]: string[];
}

interface Trackers {
	[key: string]: string[];
}

export interface AppFullDetails {
	myapp: {
		streamed: Promise<AppFullDetail>;
	};
	status?: number;
	error?: string;
	myranks: {
		streamed: Promise<{ latest: AppRankDetail[]; history: AppRankDetail[] }>;
	};
	myPackageInfo: {
		streamed: Promise<{
			permissions: string[];
			trackers: Trackers;
			networks: Networks;
			android: string[];
			leftovers: string[];
		}>;
	};
}

export interface TrackerDetail {
	tracker_name: string;
	app_count: number;
	percent: number;
}
export interface TopTrackersInfo {
	status?: number;
	error?: string;
	trackers: {
		streamed: Promise<{ trackers: TrackerDetail[] }>;
	};
}

export interface NetworkDetail {
	network_name: string;
	app_count: number;
	percent: number;
}

export interface TopNetworksInfo {
	status?: number;
	error?: string;
	networks: {
		streamed: Promise<{ networks: NetworkDetail[] }>;
	};
}
export interface AppHistoryInfo {
	crawled_date: string;
	review_count: number;
	rating: number;
	installs: number;
	country: string;
	rating_count: number;
}

export interface AppFullDetail {
	icon_url_512?: string;
	name: string;
	installs?: string;
	store_id: string;
	id: number;
	developer_id?: string;
	developer_name: string;
	store_link: string;
	store_developer_link?: string;
	developer_url?: string;
	updated_at: string;
	rating?: number;
	rating_count: string;
	review_count: string;
	histogram: number[];
	rating_count_num: number;
	category: string;
	free: string;
	price: string;
	size?: string;
	minimum_android?: string;
	developer_email?: string;
	content_rating?: string;
	ad_supported?: string;
	in_app_purchases?: string;
	editors_choice?: string;
	crawl_result: string;
	release_date: string;
	store_last_updated: string;
	created_at: string;
	history_table: AppHistoryInfo[];
	featured_image_url?: string;
	phone_image_url_1?: string;
	phone_image_url_2?: string;
	phone_image_url_3?: string;
	tablet_image_url_1?: string;
	tablet_image_url_2?: string;
	tablet_image_url_3?: string;
	historyData?: { numbers: ChartTabularData; changes: ChartTabularData };
}

export type CategoryRanks = {
	category_id: number;
	category_name: string;
};

export type CollectionRanks = {
	collection_id: number;
	collection_name: string;
	categories: CategoryRanks[];
};

export type Store = {
	store_id: number;
	store_name: string;
	collections: CollectionRanks[];
};

export type StoreRankingsMap = {
	stores_rankings: Store[];
};
