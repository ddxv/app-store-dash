import type { LayoutServerLoad } from './$types';

interface LoadResponse {
    mycats: any;
    status?: number;
    error?: string;
}

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<LoadResponse> {
    console.log('load categories started');
    try {

        const res = await fetch(`http://localhost:8000/api/categories`);

        if (!res.ok) {
            throw new Error(`Failed to fetch categories with status ${res.status}`);
        }

        const categories = await res.json();
        console.log(`loaded categories with len: ${Object.keys(categories).length}`);
        return { mycats: categories };

    } catch (error) {
        console.error('Failed to load data:', error);
        return {
            mycats: null,
            status: 500,
            error: 'Failed to load categories'
        };
    }
}



export const ssr = true;
export const csr = true;
