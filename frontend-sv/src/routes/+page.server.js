export const ssr = true;
export const csr = true;
console.log('Script executed');
/** @type {import('./$types').PageServerLoad} */
export async function load() {
    console.log('load started'); try {
        const res = await fetch('http://localhost:8000/api/apps');

        if (!res.ok) {
            throw new Error(`Failed to fetch with status ${res.status}`);
        }

        const trending_apps = await res.json();
        console.log(`loaded trending_apps with len: ${Object.keys(trending_apps).length}`);
        return { thing: trending_apps };
    } catch (error) {
        console.error('Failed to load data:', error);
        return {
            status: 500,
            error: 'Failed to load trending apps'
        };
    }
}

