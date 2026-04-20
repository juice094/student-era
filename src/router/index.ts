import { createRouter, createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'),
    meta: { title: '首页概览' }
  },
  {
    path: '/student',
    name: 'Student',
    component: () => import('@/views/StudentView.vue'),
    meta: { title: '学生管理' }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutView.vue'),
    meta: { title: '关于系统' }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
