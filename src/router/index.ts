import { createRouter, createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useUserStore } from '@/stores/user'

const routes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue'),
    meta: { public: true, title: '登录' }
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'),
    meta: { title: '首页概览', icon: 'HomeFilled', menu: 'Home' }
  },
  {
    path: '/student',
    name: 'Student',
    component: () => import('@/views/StudentView.vue'),
    meta: { title: '学生管理', icon: 'UserFilled', menu: 'Student' }
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: () => import('@/views/TeacherView.vue'),
    meta: { title: '教师管理', icon: 'UserFilled', menu: 'Teacher' }
  },
  {
    path: '/course',
    name: 'Course',
    component: () => import('@/views/CourseView.vue'),
    meta: { title: '课程管理', icon: 'Reading', menu: 'Course' }
  },
  {
    path: '/score',
    name: 'Score',
    component: () => import('@/views/ScoreView.vue'),
    meta: { title: '成绩管理', icon: 'TrendCharts', menu: 'Score' }
  },
  {
    path: '/course-select',
    name: 'CourseSelect',
    component: () => import('@/views/CourseSelectView.vue'),
    meta: { title: '学生选课', icon: 'Plus', menu: 'CourseSelect' }
  },
  {
    path: '/schedule',
    name: 'Schedule',
    component: () => import('@/views/ScheduleView.vue'),
    meta: { title: '排课管理', icon: 'Calendar', menu: 'Schedule' }
  },
  {
    path: '/evaluation',
    name: 'Evaluation',
    component: () => import('@/views/EvaluationView.vue'),
    meta: { title: '评教结果', icon: 'Star', menu: 'Evaluation' }
  },
  {
    path: '/operation-log',
    name: 'OperationLog',
    component: () => import('@/views/OperationLogView.vue'),
    meta: { title: '操作日志', icon: 'Document', menu: 'OperationLog' }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutView.vue'),
    meta: { title: '关于系统', icon: 'InfoFilled', menu: 'About' }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to) => {
  const userStore = useUserStore()

  // 设置页面标题
  document.title = `${String(to.meta.title || '页面')} — 教务可视化系统`

  // 公开页面直接放行
  if (to.meta.public) {
    return true
  }

  // 未登录跳登录页
  if (!userStore.isLoggedIn) {
    return '/login'
  }

  // 检查菜单权限
  const menuCode = to.meta.menu as string
  if (menuCode && !userStore.checkMenu(menuCode)) {
    return '/'
  }

  return true
})

export default router
