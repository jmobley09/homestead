/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'
import Home from '@/views/Home.vue'
import Pantry from '@/views/Pantry.vue'
import ShoppingList from '@/views/ShoppingList.vue'

// Composables
import { createApp } from 'vue'
import {createRouter, createWebHistory } from 'vue-router'

// Plugins
import { registerPlugins } from '@/plugins'

const router = createRouter( {
    history: createWebHistory(),
    routes: [
        {path: '/', component: Home},
        {path: '/pantry', component: Pantry},
        {path: '/shopping-list', component: ShoppingList}
    ]
})

const app = createApp(App)

registerPlugins(app)

app.use(router)

app.mount('#app')
