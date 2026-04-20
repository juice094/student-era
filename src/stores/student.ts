import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Student, ScoreDistribution } from '@/types'
import { fetchStudentList, fetchScoreDistribution } from '@/api/modules/student'

export const useStudentStore = defineStore('student', () => {
  const students = ref<Student[]>([])
  const scoreDistribution = ref<ScoreDistribution[]>([])
  const loading = ref(false)

  async function loadStudents() {
    loading.value = true
    try {
      const res = await fetchStudentList()
      students.value = res.data
    } finally {
      loading.value = false
    }
  }

  async function loadScoreDistribution() {
    loading.value = true
    try {
      const res = await fetchScoreDistribution()
      scoreDistribution.value = res.data
    } finally {
      loading.value = false
    }
  }

  return {
    students,
    scoreDistribution,
    loading,
    loadStudents,
    loadScoreDistribution
  }
})
