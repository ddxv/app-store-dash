import type { ChartTabularData } from '@carbon/charts-svelte';
import type { Row } from '@vincjo/datatables/remote';

export type Crumb<M = any> = {
	title?: string;
	url?: string;
	metadata?: M;
};
export type ModuleData = {
	pageTitle?: string;
	getPageTitle?: (data: any) => string;
};

export type MyCrumbMetadata = {
	extraValue: string;
};

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

export interface PlaystoreSearchResponse {
	results: AppGroup;
	status?: number;
	error?: string;
}
export interface AppleStoreSearchResponse {
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

export interface RankedApps extends Row {
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

export interface AppHistoryInfo extends Row {
	crawled_date: string;
	review_count: number;
	rating: number;
	installs: number;
	country: string;
	rating_count: number;
}
export interface AdsTxtEntries extends Row {
	company_name: string;
	ad_domain: number;
	ad_domain_url: string;
	publisher_id: string;
	relationship: string;
	crawl_result: string;
	developer_domain_crawled_at: number;
}

export interface CompaniesOverviewEntries extends Row {
	ad_network: string;
	tag_source: string;
	store: string;
	app_count: number;
}

export interface CompaniesOverviewPlatforms extends Row {
	android: CompaniesOverviewEntries[];
	ios: CompaniesOverviewEntries[];
	top: {
		group: string;
		value: number;
	}[];
}

export interface CompaniesOverviewSections extends Row {
	sdk: CompaniesOverviewPlatforms;
	adstxt: CompaniesOverviewPlatforms;
	categories: CompanyCategoryOverview;
}

export interface CompaniesOverview {
	status?: number;
	error?: string;
	companiesOverview: CompaniesOverviewSections;
}

export interface OverviewAppList {
	apps: CompanyOverviewApps[];
}

export interface CompanyOverviewApps extends Row {
	//del
	rank: number;
	name: string;
	store_id: string;
}

export interface CompanyOverviewPlatforms {
	android: OverviewAppList;
	ios: OverviewAppList;
}

export interface CompanyOverviewSections {
	sdk: CompanyOverviewPlatforms;
	adstxt: CompanyOverviewPlatforms;
}

export interface CategoryAppStats {
	sdk_ios_total_apps: number;
	sdk_android_total_apps: number;
	adstxt_ios_total_apps: number;
	adstxt_android_total_apps: number;
	total_apps: number;
}

export interface ChildrenCompanyTree {
	company_name: string;
	domains: string[];
}

export interface ParentCompanyTree {
	parent_company_name: string | null;
	company_name: string;
	domains: string[];
	children_companies: ChildrenCompanyTree[];
}

export interface CompanyPatterns {
	package_patterns: string[];
	paths: string[];
}

export interface CompanyPatternsDict {
	companies: {
		[company_name: string]: CompanyPatterns;
	};
}

export interface CompanyCategoryOverview {
	categories: {
		[key: string]: CategoryAppStats;
	};
}

export interface CompanyFullDetails {
	status?: number;
	error?: string;
	companyDetails: CompanyCategoryOverview;
	companyTopApps: CompanyOverviewSections;
	companyTree: ParentCompanyTree;
	companySdks: CompanyPatternsDict;
	companyParentCategories: ChartTabularData;
}
export interface CompanyCategoryDetails {
	status?: number;
	error?: string;
	companyDetails: CompanyCategoryOverview;
	companyCategoryApps: CompanyOverviewSections;
	companyTree: ParentCompanyTree;
}

export interface AppFullDetails {
	myapp: AppFullDetail;
	status?: number;
	error?: string;
	myranks: Promise<{ latest: AppRankDetail[]; history: AppRankDetail[] }>;
	myhistory: Promise<{
		histogram: number[];
		history_table: AppHistoryInfo[];
		plot_data?: {
			numbers: ChartTabularData;
			changes: ChartTabularData;
			installs: ChartTabularData;
			ratings: ChartTabularData;
		};
	}>;
	myPackageInfo: Promise<{
		permissions: string[];
		trackers: Trackers;
		networks: Networks;
		android: string[];
		leftovers: UnknownManifestItems;
	}>;
	myAdsTxt: Promise<{
		direct_entries: AdsTxtEntries[];
		reseller_entries: AdsTxtEntries[];
	}>;
}

export interface CategoriesAdtech {
	[store: number]: { [category: string]: Company[] };
}

export interface Company {
	name: string;
	app_count: number;
	installs: number;
	ratings: number;
	installs_percent: number;
	ratings_percent: number;
	app_count_percent: number;
}

export interface TopCompaniesInfo {
	status?: number;
	error?: string;
	networks: Promise<{
		all_companies: CategoriesAdtech;
		parent_companies: CategoriesAdtech;
	}>;
	trackers: Promise<{
		all_companies: CategoriesAdtech;
		parent_companies: CategoriesAdtech;
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
