import { defineStore } from "pinia";
import { mande } from "mande";
import _ from 'lodash';

const api = mande('http://localhost:8081');

export const usePantryStore = defineStore('pantry', {
    state: () => {
        return {
            data: []
        }
    },
    getters: {
        categories: (state) => _.map(state.data, 'name')
    },
    actions: {
        async fetchCategories() {
            await api.get('/categories').then((response) => {this.data = response});
        }
    }
})