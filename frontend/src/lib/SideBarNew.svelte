<script lang="ts">
	import { page } from '$app/stores';
	import SideBarCats from './SideBarCats.svelte';

	function getBaseUrl(url: string, newValue: string) {
		const parts = url.split('/').filter(Boolean);
		let newUrl = url;

		if (parts[0] === 'companies') {
			if (parts.length == 1) {
				// This triggers on /companies
				// console.log("newURL hardcoded");
				newUrl = '/companies/categories';
			} else if (parts.length == 2) {
				// this is not used
			} else if (parts.length == 3) {
				console.log('newValue', newValue);
				if (parts[2] == 'overall') {
					newUrl = `/companies/${parts[1]}`;
				} else {
					// this is working on /companies/[company]/[category]
					// this is working on /companies/categories[category]
					// console.log("newURL 3", parts.slice(2).join('/'));
					newUrl = `/companies/${parts[1]}`;
				}
			}
		}
		// console.log("newURL",newUrl);

		return newUrl;
	}

	$: baseUrl = getBaseUrl($page.url.pathname.toString(), $page.params.category);

	import type { CatData } from '../types';
	export let myCatData: CatData;
</script>

<SideBarCats {myCatData} {baseUrl} />
