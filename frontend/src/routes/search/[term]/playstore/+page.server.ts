// import type { PageServerLoad } from './$types.js';
import type { PageServerLoad, Actions } from './$types';
// import * as gplay from 'google-play-scraper';
import gplay from 'google-play-scraper'; // Correct: default import

export const ssr: boolean = true;

export const load: PageServerLoad = async ({ params }) => {
    const term = params.term;
    const searchTerm = decodeURIComponent(term);
    console.log(`search start term=${searchTerm}`);

    try {
        const response = await gplay.search({
            term: searchTerm,
            num: 5 // Adjust the number of results as needed
        });
        return { results: response }; 
    } catch (error) {
        console.log('Uncaught error', error);
        return { results: 'Uncaught Error' };
    }
};

