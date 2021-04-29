import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
  { path: '/', component: 'Recommend' },
  { path: '/emoji', component: 'Emoji' },
  { path: '*', component: 'NotFound' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
