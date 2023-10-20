import { writable } from 'svelte/store';

console.log(`stores start`);

export interface Categories {
    mycats: any;
    status?: number;
    error?: string;
}

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<Categories> {
    console.log(`stores load categories start`);
    try {

        const res = await fetch(`http://localhost:8000/api/categories`);

        if (!res.ok) {
            throw new Error(`Failed to fetch categories with status ${res.status}`);
        }

        const categories = await res.json();

        console.log(`stores loaded categories with len: ${Object.keys(categories).length}`);
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

const defaultCategories: Categories = {
    mycats: [],
    status: 200,
    error: ''
};


// export const myList = writable<Categories | null>(null);
export const myList = writable<Categories>(defaultCategories);

console.log("stores myList try set")

load().then(result => {
    myList.set(result);
    console.log("stores myList set!")
});

console.log("stores done")