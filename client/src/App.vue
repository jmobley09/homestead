<script setup lang="ts">
import Navbar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <div>
    <div class="min-h-screen">
      <Navbar />
      <RouterView />
    </div>
    <Footer />
  </div>
</template>
