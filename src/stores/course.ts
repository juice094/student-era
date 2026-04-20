import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Course } from '@/types/course'
import { persist, restore } from '@/utils/persist'

const PERSIST_KEY = 'courses'

const mockCourses: Course[] = [
  { id: 1, courseNo: 'CS101', name: '计算机导论', credit: 3, hours: 48, type: '必修', collegeId: 1, collegeName: '信息工程学院', teacherId: 1, teacherName: '王教授', semester: '2024-2025-1', maxStudents: 120, description: '计算机专业入门课程' },
  { id: 2, courseNo: 'CS201', name: '数据结构', credit: 4, hours: 64, type: '必修', collegeId: 1, collegeName: '信息工程学院', teacherId: 1, teacherName: '王教授', semester: '2024-2025-1', maxStudents: 100 },
  { id: 3, courseNo: 'CS301', name: '操作系统', credit: 4, hours: 64, type: '必修', collegeId: 1, collegeName: '信息工程学院', teacherId: 2, teacherName: '李副教授', semester: '2024-2025-1', maxStudents: 80 },
  { id: 4, courseNo: 'EC101', name: '经济学原理', credit: 3, hours: 48, type: '必修', collegeId: 2, collegeName: '经济管理学院', teacherId: 3, teacherName: '张老师', semester: '2024-2025-1', maxStudents: 150 },
  { id: 5, courseNo: 'ME101', name: '机械设计基础', credit: 3.5, hours: 56, type: '必修', collegeId: 3, collegeName: '机械工程学院', teacherId: 4, teacherName: '刘老师', semester: '2024-2025-1', maxStudents: 90 },
  { id: 6, courseNo: 'CS401', name: '人工智能导论', credit: 2, hours: 32, type: '选修', collegeId: 1, collegeName: '信息工程学院', teacherId: 5, teacherName: '陈老师', semester: '2024-2025-1', maxStudents: 200 }
]

export const useCourseStore = defineStore('course', () => {
  const courses = ref<Course[]>([])

  function loadCourses() {
    if (courses.value.length === 0) {
      courses.value = restore<Course[]>(PERSIST_KEY, mockCourses)
    }
  }

  function addCourse(c: Course) {
    courses.value.push(c)
    persist(PERSIST_KEY, courses.value)
  }

  function updateCourse(c: Course) {
    const idx = courses.value.findIndex((item) => item.id === c.id)
    if (idx !== -1) {
      courses.value[idx] = c
      persist(PERSIST_KEY, courses.value)
    }
  }

  function deleteCourse(id: number) {
    const idx = courses.value.findIndex((item) => item.id === id)
    if (idx !== -1) {
      courses.value.splice(idx, 1)
      persist(PERSIST_KEY, courses.value)
    }
  }

  return {
    courses,
    loadCourses,
    addCourse,
    updateCourse,
    deleteCourse
  }
})
