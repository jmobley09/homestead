<template>
  <v-card>
    <v-card-title class="d-flex justify-center">Pantry</v-card-title>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
        title="Item"
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
      ></v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>

<script>
export default {
  name: "Pantry",
};
</script>
<style scoped>
</style>