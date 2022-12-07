import type { RouteRecordRaw } from "vue-router";
import { createRouter, createWebHistory } from "vue-router";
import NProgress from "nprogress";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: () => import("~/views/Home.vue"),
  },
  {
    path: "/404",
    name: "ErrorPage",
    component: () => import("~/views/errorPage.vue"),
  },
  {
    path: "/home",
    name: "Home",
    component: () => import("~/views/Home.vue"),
  },
  {
    path: "/StoreTest",
    name: "StoreTest",
    component: () => import("~/views/home/components/StoreTest.vue"),
  },
  {
    path: "/pantry",
    name: "Pantry",
    component: () => import("~/views/Pantry.vue"),
  },
  {
    path: "/shopping-list",
    name: "ShoppingList",
    component: () => import("~/views/ShoppingList.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
  },
];

const index = createRouter({
  history: createWebHistory(),
  routes,
});
index.beforeEach(() => {
  if (!NProgress.isStarted()) {
    NProgress.start();
  }
});

index.afterEach(() => {
  NProgress.done();
});

export default index;
