<template>
<div>
  <NavDrawer></NavDrawer>
  <router-view class="view"></router-view>
</div>
</template>

<script setup>
// import HelloWorld from '@/components/HelloWorld.vue'
import NavDrawer from "@/components/NavDrawer.vue";
</script>
<style scoped>
.view {
  margin-left: 300px;
}
</style>
