import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import Contact from "../views/Contact.vue";

import {firebaseApp} from "../services/firebaseService";
import {getAuth} from "firebase/auth";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
    meta: {
      requireAuth: true
    }
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  const requireAuth = to.matched.some(record => record.meta.requireAuth);
  const auth = getAuth(firebaseApp)
  const isAuthenticated = auth.currentUser

  if (!isAuthenticated && requireAuth){
    next("/");
  }else{
    next();
  }
})

export default router;
