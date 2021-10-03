import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

import {firebaseApp} from './services/firebaseService'
import {getAuth} from 'firebase/auth'

Vue.config.productionTip = false;

const auth = getAuth(firebaseApp)

let app;

auth.onAuthStateChanged(user => {
  /* teste user log */
  console.log(user)
  if(!app){
    app = new Vue({
      router,      
      store,
      vuetify,
      render: (h) => h(App),
    }).$mount("#app");
  }
})