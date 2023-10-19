export const ssr: boolean = true;
export const csr: boolean = false;
console.log('Script executed');

interface LoadResponse {
    myapps: any; // Replace 'any' with the expected structure of the trending_apps if known
    status?: number;
    error?: string;
}

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<LoadResponse> {
    console.log('load started');
    try {
        const res = await fetch('http://localhost:8000/api/apps');

        if (!res.ok) {
            throw new Error(`Failed to fetch with status ${res.status}`);
        }

        const trending_apps: any = await res.json(); // Replace 'any' with the expected structure of the trending_apps if known
        console.log(`loaded trending_apps with len: ${Object.keys(trending_apps).length}`);
        return { myapps: trending_apps };
    } catch (error) {
        console.error('Failed to load data:', error);
        return {
            myapps: {},
            status: 500,
            error: 'Failed to load trending apps'
        };
    }
}
