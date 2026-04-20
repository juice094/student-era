import type { UserRole } from '@/types/user'

export const ROLE_NAMES: Record<UserRole, string> = {
  admin: '管理员',
  teacher: '教师',
  student: '学生'
}

export const MENU_PERMISSIONS: Record<UserRole, string[]> = {
  admin: ['Home', 'Student', 'Teacher', 'Course', 'Score', 'CourseSelect', 'Schedule', 'Evaluation', 'OperationLog', 'About'],
  teacher: ['Home', 'Student', 'Teacher', 'Course', 'Score', 'Evaluation', 'About'],
  student: ['Home', 'Course', 'Score', 'CourseSelect', 'Evaluation', 'About']
}

export const BUTTON_PERMISSIONS: Record<string, string[]> = {
  'student:add': ['admin'],
  'student:edit': ['admin', 'teacher'],
  'student:delete': ['admin'],
  'teacher:add': ['admin'],
  'teacher:edit': ['admin'],
  'teacher:delete': ['admin'],
  'course:add': ['admin'],
  'course:edit': ['admin'],
  'course:delete': ['admin'],
  'score:enter': ['admin', 'teacher'],
  'score:audit': ['admin'],
  'course:arrange': ['admin'],
  'course:select': ['student'],
  'dict:manage': ['admin'],
  'evaluation:view': ['admin', 'teacher'],
  'schedule:manage': ['admin'],
  'log:view': ['admin']
}

export function hasRole(role: UserRole, requiredRoles: UserRole[]): boolean {
  return requiredRoles.includes(role)
}

export function hasMenu(role: UserRole, menuName: string): boolean {
  return MENU_PERMISSIONS[role]?.includes(menuName) ?? false
}

export function hasButton(role: UserRole, buttonCode: string): boolean {
  const allowed = BUTTON_PERMISSIONS[buttonCode]
  return allowed ? allowed.includes(role) : false
}
