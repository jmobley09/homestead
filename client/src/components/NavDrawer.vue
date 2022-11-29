<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer>
        <v-list>
          <router-link to="/pantry"
            ><v-list-item
              prepend-icon="mdi-folder"
              title="Pantry"
            ></v-list-item
          ></router-link>
          <router-link to="/shopping-list"
            ><v-list-item
              prepend-icon="mdi-account-multiple"
              title="Shopping List"
            ></v-list-item
          ></router-link>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </v-card>
</template>
<script>
export default {
  name: "NavDrawer",
};
</script>