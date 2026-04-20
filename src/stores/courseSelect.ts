import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export interface CourseSelectRecord {
  id: number
  studentId: number
  studentName: string
  courseId: number
  courseName: string
  courseNo: string
  credit: number
  teacherName: string
  semester: string
  status: 'selected' | 'dropped'
  selectTime: string
}

export const useCourseSelectStore = defineStore('courseSelect', () => {
  const records = ref<CourseSelectRecord[]>([])

  const mockRecords: CourseSelectRecord[] = [
    { id: 1, studentId: 2021001, studentName: '张伟', courseId: 1, courseName: '计算机导论', courseNo: 'CS101', credit: 3, teacherName: '王教授', semester: '2024-2025-1', status: 'selected', selectTime: '2024-09-01 10:00' },
    { id: 2, studentId: 2021001, studentName: '张伟', courseId: 2, courseName: '数据结构', courseNo: 'CS201', credit: 4, teacherName: '王教授', semester: '2024-2025-1', status: 'selected', selectTime: '2024-09-01 10:05' },
    { id: 3, studentId: 2021002, studentName: '李娜', courseId: 1, courseName: '计算机导论', courseNo: 'CS101', credit: 3, teacherName: '王教授', semester: '2024-2025-1', status: 'selected', selectTime: '2024-09-01 11:00' },
    { id: 4, studentId: 2022001, studentName: '刘洋', courseId: 4, courseName: '经济学原理', courseNo: 'EC101', credit: 3, teacherName: '张老师', semester: '2024-2025-1', status: 'selected', selectTime: '2024-09-02 09:00' }
  ]

  function loadRecords() {
    if (records.value.length === 0) {
      records.value = mockRecords
    }
  }

  function selectCourse(r: CourseSelectRecord) {
    records.value.push(r)
  }

  function dropCourse(id: number) {
    const idx = records.value.findIndex((item) => item.id === id)
    if (idx !== -1) records.value[idx].status = 'dropped'
  }

  function getMyCourses(studentId: number): CourseSelectRecord[] {
    return records.value.filter((r) => r.studentId === studentId && r.status === 'selected')
  }

  const selectedCount = computed(() => records.value.filter((r) => r.status === 'selected').length)
  const totalCredits = computed(() =>
    records.value.filter((r) => r.status === 'selected').reduce((sum, r) => sum + r.credit, 0)
  )

  return {
    records,
    selectedCount,
    totalCredits,
    loadRecords,
    selectCourse,
    dropCourse,
    getMyCourses
  }
})
