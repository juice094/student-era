import { defineStore } from 'pinia'
import { ref } from 'vue'
import { persist, restore } from '@/utils/persist'

export interface OperationLog {
  id: number
  username: string
  realName: string
  role: string
  module: string
  action: string
  detail: string
  ip: string
  time: string
  status: 'success' | 'fail'
}

const PERSIST_KEY = 'operation_logs'

const mockLogs: OperationLog[] = [
  { id: 1, username: 'admin', realName: '系统管理员', role: 'admin', module: '学生管理', action: '新增学生', detail: '新增学生: 张伟 (2021001)', ip: '192.168.1.10', time: '2024-09-15 10:23:45', status: 'success' },
  { id: 2, username: 'teacher', realName: '张老师', role: 'teacher', module: '成绩管理', action: '录入成绩', detail: '为课程 CS101 录入 35 条成绩', ip: '192.168.1.25', time: '2024-09-15 14:12:08', status: 'success' },
  { id: 3, username: 'admin', realName: '系统管理员', role: 'admin', module: '课程管理', action: '删除课程', detail: '删除课程: 离散数学 (CS301)', ip: '192.168.1.10', time: '2024-09-15 16:45:22', status: 'success' },
  { id: 4, username: 'student', realName: '李同学', role: 'student', module: '选课系统', action: '选课', detail: '选修课程: 人工智能导论 (CS401)', ip: '192.168.1.56', time: '2024-09-16 09:08:33', status: 'success' },
  { id: 5, username: 'teacher', realName: '张老师', role: 'teacher', module: '成绩管理', action: '修改成绩', detail: '修改学生 2021003 的成绩为 85 分', ip: '192.168.1.25', time: '2024-09-16 11:30:15', status: 'success' },
  { id: 6, username: 'admin', realName: '系统管理员', role: 'admin', module: '系统管理', action: '登录', detail: '管理员登录系统', ip: '192.168.1.10', time: '2024-09-16 08:00:01', status: 'success' },
  { id: 7, username: 'student', realName: '李同学', role: 'student', module: '选课系统', action: '退课', detail: '退选课程: 经济学原理 (EC101)', ip: '192.168.1.56', time: '2024-09-16 15:22:18', status: 'fail' }
]

export const useLogStore = defineStore('log', () => {
  const logs = ref<OperationLog[]>([])

  function loadLogs() {
    if (logs.value.length === 0) {
      logs.value = restore<OperationLog[]>(PERSIST_KEY, mockLogs)
    }
  }

  function addLog(log: OperationLog) {
    logs.value.unshift(log)
    persist(PERSIST_KEY, logs.value)
  }

  return { logs, loadLogs, addLog }
})
