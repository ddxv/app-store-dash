import type { ChartTabularData } from '@carbon/charts-svelte';
import type { Row } from '@vincjo/datatables/legacy';

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
	companiesResults: CompaniesOverviewEntries[];
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
	appCats: Promise<CatData>;
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
	topCompanies: TopCompaniesShort;
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
	company_domain: string;
	company_name: string;
	tag_source: string;
	store: string;
	app_count: number;
	percentage: number;
}

export interface CompaniesOverviewPlatforms {
	top: {
		group: string;
		value: number;
	}[];
}

export interface TopCompaniesOverview {
	sdk: CompaniesOverviewPlatforms[];
	adstxt_direct: CompaniesOverviewPlatforms[];
	adstxt_reseller: CompaniesOverviewPlatforms[];
}

export interface TopCompaniesShort {
	adnetworks: TopCompaniesOverview;
	attribution: TopCompaniesOverview;
	analytics: TopCompaniesOverview;
}

export interface CompaniesOverviewSections {
	companies_overview: CompaniesOverviewEntries[];
	top: TopCompaniesOverview;
	categories: CompaniesCategoryOverview;
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
	rank: number;
	name: string;
	store_id: string;
}

export interface SdksOverview extends Row {
	store: string;
	company_name: string;
	company_domain: string;
	xml_path: string;
	value_name: string;
	app_count: number;
}

export interface SdkOverview extends Row {
	xml_path: string;
	value_name: string;
	store: string;
	store_id: string;
	app_name: string;
	installs: number;
	rating_count: number;
}

export interface CompanyOverviewPlatforms {
	android: OverviewAppList;
	ios: OverviewAppList;
}

export interface CompanyOverviewSections {
	sdk: CompanyOverviewPlatforms;
	adstxt_direct: CompanyOverviewPlatforms;
	adstxt_reseller: CompanyOverviewPlatforms;
}

export interface CategoryCompaniesStats {
	sdk_ios_total_companies: number;
	sdk_android_total_companies: number;
	adstxt_direct_ios_total_companies: number;
	adstxt_direct_android_total_companies: number;
	adstxt_reseller_ios_total_companies: number;
	adstxt_reseller_android_total_companies: number;
	total_companies: number;
}

export interface CategoryAppStats {
	sdk_ios_total_apps: number;
	sdk_android_total_apps: number;
	adstxt_direct_ios_total_apps: number;
	adstxt_direct_android_total_apps: number;
	adstxt_reseller_ios_total_apps: number;
	adstxt_reseller_android_total_apps: number;
	total_apps: number;
}

export interface ChildrenCompanyTree {
	company_name: string;
	domains: string[];
}

export interface ParentCompanyTree {
	parent_company_name: string;
	parent_company_domain: string;
	queried_company_domain: string;
	queried_company_name: string;
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

export interface CompaniesCategoryOverview {
	categories: {
		[key: string]: CategoryCompaniesStats;
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
	companyTypes: { types: companyType[] };
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
		company_categories: { [key: string]: { [key: string]: string[] } };
		android: string[];
		leftovers: UnknownManifestItems;
	}>;
	myAdsTxt: Promise<{
		direct_entries: AdsTxtEntries[];
		reseller_entries: AdsTxtEntries[];
	}>;
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

export interface companyType {
	name: string;
	url_slug: string;
}

export interface CompaniesLayoutResponse {
	appCats: Promise<CatData>;
	companyTypes: Promise<{ types: companyType[] }>;
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
