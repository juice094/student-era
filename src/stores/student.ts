import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Student } from '@/types'
import { persist, restore } from '@/utils/persist'

const PERSIST_KEY = 'students'

const mockStudents: Student[] = [
  { id: 2021001, name: '张伟', gender: '男', age: 21, major: '计算机科学与技术', grade: '大三', enrollmentYear: 2021 },
  { id: 2021002, name: '李娜', gender: '女', age: 20, major: '软件工程', grade: '大三', enrollmentYear: 2021 },
  { id: 2021003, name: '王强', gender: '男', age: 22, major: '电子信息工程', grade: '大四', enrollmentYear: 2020 },
  { id: 2022001, name: '刘洋', gender: '女', age: 20, major: '经济管理', grade: '大二', enrollmentYear: 2022 },
  { id: 2022002, name: '陈明', gender: '男', age: 19, major: '机械工程', grade: '大二', enrollmentYear: 2022 },
  { id: 2023001, name: '赵雪', gender: '女', age: 18, major: '土木工程', grade: '大一', enrollmentYear: 2023 },
  { id: 2023002, name: '孙涛', gender: '男', age: 19, major: '艺术设计', grade: '大一', enrollmentYear: 2023 },
  { id: 2021004, name: '周敏', gender: '女', age: 21, major: '外语', grade: '大三', enrollmentYear: 2021 },
  { id: 2020001, name: '吴磊', gender: '男', age: 23, major: '计算机科学与技术', grade: '大四', enrollmentYear: 2020 },
  { id: 2022003, name: '郑丽', gender: '女', age: 20, major: '软件工程', grade: '大二', enrollmentYear: 2022 }
]

export const useStudentStore = defineStore('student', () => {
  const students = ref<Student[]>([])

  function loadStudents() {
    if (students.value.length === 0) {
      students.value = restore<Student[]>(PERSIST_KEY, mockStudents)
    }
  }

  function addStudent(s: Student) {
    students.value.push(s)
    persist(PERSIST_KEY, students.value)
  }

  function updateStudent(s: Student) {
    const idx = students.value.findIndex((item) => item.id === s.id)
    if (idx !== -1) {
      students.value[idx] = s
      persist(PERSIST_KEY, students.value)
    }
  }

  function deleteStudent(id: number) {
    const idx = students.value.findIndex((item) => item.id === id)
    if (idx !== -1) {
      students.value.splice(idx, 1)
      persist(PERSIST_KEY, students.value)
    }
  }

  return {
    students,
    loadStudents,
    addStudent,
    updateStudent,
    deleteStudent
  }
})
