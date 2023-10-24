export const ssr = true;
export const csr = false;

export interface Categories {
    mycats: any;
    status?: number;
    error?: string;
}






/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<Categories> {
    console.log(`load categories start`);
    try {

        const res = await fetch(`http://localhost:8000/api/categories`);

        if (!res.ok) {
            throw new Error(`Failed to fetch categories with status ${res.status}`);
        }

        const categories = await res.json();

        console.log(`load categories len: ${Object.keys(categories).length}`);
        return { mycats: categories };

    } catch (error) {
        console.error('Failed to load layout categories data:', error);
        return {
            mycats: null,
            status: 500,
            error: 'Failed to load categories'
        };
    }
}

