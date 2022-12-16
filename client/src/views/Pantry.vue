<template>
    <div class="hero mt-[-4rem] min-h-screen">
        <div class="hero-overlay from-primary to-base-100 bg-gradient-to-bl" />
        <div class="text-left">
            <div class="card bg-base-100 shadow-xl">
                <div class="card-body">
                    <h2 class="card-title">Pantry Items</h2>
                    <p>All the Items currently in the pantry</p>
                    <Table :headers="pantryHeaders" :data="pantry"/>
                    <div class="card-actions justify-center">
                        <button class="btn btn-primary">Add More</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { usePantryStore } from '~/store/pantry';
import { onMounted, ref, computed } from 'vue';
import Table from '../components/Table.vue';

const store = usePantryStore();
const pantry = computed(() => store.data);
const pantryHeaders = ['Name', 'Category', 'Quantity'];

onMounted(async () => {
    await store.fetchCategories();
})

</script>