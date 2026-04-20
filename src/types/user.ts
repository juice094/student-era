export type UserRole = 'admin' | 'teacher' | 'student'

export interface UserInfo {
  id: number
  username: string
  realName: string
  role: UserRole
  avatar?: string
  deptId?: number
  deptName?: string
}

export interface LoginForm {
  username: string
  password: string
  code?: string
}

export interface LoginResult {
  token: string
  userInfo: UserInfo
}

export interface RolePermission {
  role: UserRole
  menus: string[]
  buttons: string[]
}
