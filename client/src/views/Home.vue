<script setup lang="ts">
const router = useRouter();

const testStore = () => {
  router.push({
    name: "StoreTest",
  });
};
</script>

<template>
  <div class="hero text-primary-content mt-[-4rem] min-h-screen">
    <div
      class="hero-overlay from-primary to-base-100 place-items-center bg-gradient-to-bl"
    />
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="mb-5 text-5xl font-bold">
          Vite Boot
        </h1>
        <p class="mb-5">
          Mocking up web app with Vite-Boot <sup>(speed)</sup>
        </p>
        <button class="btn-primary btn" @click="testStore">
          Test Store
        </button>
      </div>
    </div>
  </div>
</template>
