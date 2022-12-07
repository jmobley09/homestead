<template>
  <div class="hero mt-[-4rem] min-h-screen">
    <div class="hero-overlay from-primary to-base-100 place-items-center bg-gradient-to-bl" />
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="mb-5 text-5xl font-bold">
          Homestead
        </h1>
        <p class="mb-5">
          Various Tools for organizing any Homestead <sup>(BETA)</sup>
        </p>
        <p>Please select a Tool below:</p>
        <router-link to="/pantry" aria-current="page" aria-label="Homepage">
          <button class="btn-primary btn m-2">
            Pantry
          </button>
        </router-link>
        <router-link to="/shopping-list" aria-current="page" aria-label="Homepage">
          <button class="btn-primary btn m-2">
            Shopping List
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>