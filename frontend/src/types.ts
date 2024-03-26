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
	results: AppGroup;
	status?: number;
	error?: string;
}

export interface CompanyApps {
	results: AppGroup;
	status?: number;
	error?: string;
}
export interface SearchResponse {
	results: AppGroup;
	status?: number;
	error?: string;
}

export interface Collection {
	categories: AppGroup;
	title: string;
}

export interface Collections {
	AppCollections: Collection;
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
	mycats: Promise<CatData>;
	status?: number;
	error?: string;
}
export interface AppRankResponse {
	myranks?: AppRankDetail;
	status?: number;
	error?: string;
}

export interface HomeData {
	androidAppRanks: Promise<{ ranks: RankedApps[] }>;
	iOSAppRanks: Promise<{ ranks: RankedApps[] }>;
	androidGameRanks: Promise<{ ranks: RankedApps[] }>;
	iOSGameRanks: Promise<{ ranks: RankedApps[] }>;
	status?: number;
	error?: string;
}

export interface RankedAppList {
	ranks: RankedApps[];
}

export interface StoreCategoryRanks {
	ranks: Promise<{ ranks: RankedApps[] }>;
	status?: number;
	error?: string;
	history: Promise<{ history: RankedApps[] }>;
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

export interface Networks {
	[key: string]: { [key: string]: string[] };
}

export interface Trackers {
	[key: string]: { [key: string]: string[] };
}

interface UnknownManifestItems {
	[key: string]: string[];
}

export interface AppHistoryInfo {
	crawled_date: string;
	review_count: number;
	rating: number;
	installs: number;
	country: string;
	rating_count: number;
}
export interface AppFullDetails {
	myapp: AppFullDetail;
	status?: number;
	error?: string;
	myranks: Promise<{ latest: AppRankDetail[]; history: AppRankDetail[] }>;
	myhistory: Promise<{
		histogram: number[];
		history_table: AppHistoryInfo[];
		plot_data?: { numbers: ChartTabularData; changes: ChartTabularData };
	}>;
	myPackageInfo: Promise<{
		permissions: string[];
		trackers: Trackers;
		networks: Networks;
		android: string[];
		leftovers: UnknownManifestItems;
	}>;
}

export interface CategoriesAdtech {
	[category: string]: Company[];
}

export interface Company {
	name: string;
	app_count: number;
	installs?: number;
	percent: number;
}

export interface TopCompaniesInfo {
	status?: number;
	error?: string;
	networks: Promise<{
		all_companies: CategoriesAdtech;
		parent_companies: CategoriesAdtech;
		monthly_all_companies: CategoriesAdtech;
		monthly_parent_companies: CategoriesAdtech;
	}>;
	trackers: Promise<{
		all_companies: CategoriesAdtech;
		parent_companies: CategoriesAdtech;
		monthly_all_companies: CategoriesAdtech;
		monthly_parent_companies: CategoriesAdtech;
	}>;
	mycats: Promise<CatData>;
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
	featured_image_url?: string;
	phone_image_url_1?: string;
	phone_image_url_2?: string;
	phone_image_url_3?: string;
	tablet_image_url_1?: string;
	tablet_image_url_2?: string;
	tablet_image_url_3?: string;
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
