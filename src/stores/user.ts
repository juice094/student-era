import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { UserInfo, UserRole, LoginForm } from '@/types/user'
import { getToken, setToken, getUserInfo, setUserInfo, clearAuth } from '@/utils/auth'
import { hasMenu, hasButton } from '@/utils/permission'

// Mock 登录 API（后续替换为真实 API）
const MOCK_USERS: Record<string, { password: string; info: UserInfo }> = {
  admin: {
    password: 'admin123',
    info: { id: 1, username: 'admin', realName: '系统管理员', role: 'admin' }
  },
  teacher: {
    password: 'teacher123',
    info: { id: 2, username: 'teacher', realName: '张老师', role: 'teacher', deptName: '计算机学院' }
  },
  student: {
    password: 'student123',
    info: { id: 3, username: 'student', realName: '李同学', role: 'student', deptName: '计算机学院' }
  }
}

export const useUserStore = defineStore('user', () => {
  const token = ref<string | null>(getToken())
  const userInfo = ref<UserInfo | null>(getUserInfo())

  const isLoggedIn = computed(() => !!token.value && !!userInfo.value)
  const role = computed(() => userInfo.value?.role ?? null)
  const isAdmin = computed(() => role.value === 'admin')
  const isTeacher = computed(() => role.value === 'teacher')
  const isStudent = computed(() => role.value === 'student')

  async function login(form: LoginForm): Promise<boolean> {
    const mock = MOCK_USERS[form.username]
    if (!mock || mock.password !== form.password) {
      throw new Error('用户名或密码错误')
    }

    const fakeToken = `mock-jwt-token-${Date.now()}`
    token.value = fakeToken
    userInfo.value = { ...mock.info }

    setToken(fakeToken)
    setUserInfo(mock.info)
    return true
  }

  function logout(): void {
    token.value = null
    userInfo.value = null
    clearAuth()
  }

  function checkMenu(menuName: string): boolean {
    if (!role.value) return false
    return hasMenu(role.value, menuName)
  }

  function checkButton(buttonCode: string): boolean {
    if (!role.value) return false
    return hasButton(role.value, buttonCode)
  }

  return {
    token,
    userInfo,
    isLoggedIn,
    role,
    isAdmin,
    isTeacher,
    isStudent,
    login,
    logout,
    checkMenu,
    checkButton
  }
})
