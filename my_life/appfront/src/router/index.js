import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/home/Home";
import archives from "../components/archives/archives";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/archives',
      name: 'archives',
      component: archives
    }
  ]
})
