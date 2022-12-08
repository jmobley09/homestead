<template>
    <div class="hero mt-[-4rem] min-h-screen">
        <div class="hero-overlay from-primary to-base-100 bg-gradient-to-bl" />
        <div class="text-left">
            <div class="card w-96 bg-base-100 shadow-xl">
                <div class="card-body">
                    <h2 class="card-title">Pantry Items</h2>
                    <p>All the Items currently in the pantry</p>
                    <div class="card-actions justify-center">
                        <button class="btn btn-primary">Add More</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { usePantryStore } from '~/store/pantry';
import { onMounted } from 'vue';

const store = usePantryStore();

onMounted(() => {
    store.fetchCategories();
    console.log(store.data);
})
</script>