import { defineStore } from "pinia";
import { mande } from "mande";

const api = mande('http://localhost:8081');

export const usePantryStore = defineStore('pantry', {
    state: () => {
        return {
            data: [] as PantryInfo[]
        }
    },
    actions: {
        async fetchCategories() {
            await api.get<PantryInfo[]>('/categories').then((response) => {this.data = response});
        }
    }
})

interface items { 
    name: string,
    id: number,
    description: string,
    quantity: number,
    owner_id: number,
}

interface PantryInfo { 
    name: string,
    id: number,
    items: items[]
}