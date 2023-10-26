import { writable } from 'svelte/store';
import type { CategoriesInfo } from './types';

export const myCollectionStore = writable('new_monthly');
export const myStoreSelection = writable('google');
export const myCategorySelection = writable('overall');

export const myCategoryMap = writable<CategoriesInfo>({ mycats: { categories: {} } });
