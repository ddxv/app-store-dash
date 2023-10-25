import { writable } from 'svelte/store';

export const myCollectionStore = writable('new_weekly');
export const myStoreSelection = writable('google');
export const myCategorySelection = writable('overall');

export const myCategoryMap = writable();
