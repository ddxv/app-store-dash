CURRENT ROUTES:
/apps/ -> list of all apps
/apps/com.specific.app-> Single app page, with links to companies

/companies/ -> list of all companies
/companies/unityads.com -> list of apps for company "unityads.com"

/companies/categories/education -> list of all companies by number of apps in this app-category

/companies/unityads.com/education -> list of apps for company "unityads.com" in this category

NEW:
/companies/types/{type}/               # List companies of specific type (e.g., tools, ad-networks)
/companies/types/{type}/apps/          # List all apps from companies of this type

/categories/{category}/                # List all apps in category
/companies/{company-id}/categories/{category}/  # List company's apps in category
/companies/types/{type}/categories/{category}/  # List apps from companies of type in category
/

OLD ROUTE (included the android/ios breakout of "Google" which i'm removing):
/adtech/companies/UA/Google/Education
/adtech/companies/?type=Networks