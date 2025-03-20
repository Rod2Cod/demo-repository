import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DomandeView from "@/views/DomandeView.vue";
import TestView from "@/views/TestView.vue";
import AggiungiDomanda from "@/views/AggiungiDomanda.vue";
import ModificaDomanda from "@/views/ModificaDomanda.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/questions',
      name: 'questions',
      component: DomandeView,
    },
    {
      path: '/addquestion',
      name: 'addquestion',
      component: AggiungiDomanda,
    },
    {
      path: '/editquestion/:id',
      name: 'editquestion',
      component: ModificaDomanda,
    },
    {
      path: '/tests',
      name: 'tests',
      component: TestView,
    },


  ],
})

export default router
