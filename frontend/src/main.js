import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import {app} from './services/firebase';

Vue.config.productionTip = false;
console.log(app)

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
