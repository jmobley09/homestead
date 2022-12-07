<script setup lang="ts">
import Navbar from "./components/layout/Navbar/index.vue";
import Footer from "./components/layout/Footer/index.vue";
</script>

<template>
  <div class="font-chinese antialiased">
    <div class="min-h-screen">
      <Navbar />
      <RouterView />
    </div>
    <Footer />
  </div>
</template>
