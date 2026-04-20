import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Score, ScoreWeight } from '@/types/score'
import { DEFAULT_WEIGHT } from '@/types/score'
import { persist, restore } from '@/utils/persist'

const PERSIST_KEY = 'scores'

function calcTotal(usual: number, midterm: number, final: number, weight: ScoreWeight): number {
  return Number((usual * weight.usual + midterm * weight.midterm + final * weight.final).toFixed(1))
}

function calcGpa(total: number): number {
  if (total >= 90) return 4.0
  if (total >= 85) return 3.7
  if (total >= 82) return 3.3
  if (total >= 78) return 3.0
  if (total >= 75) return 2.7
  if (total >= 72) return 2.3
  if (total >= 68) return 2.0
  if (total >= 64) return 1.5
  if (total >= 60) return 1.0
  return 0
}

function enrichScore(s: Score, w: ScoreWeight): Score {
  const total = calcTotal(s.usualScore, s.midtermScore, s.finalScore, w)
  return { ...s, totalScore: total, gpa: calcGpa(total) }
}

const mockScores: Score[] = [
  { id: 1, studentId: 2021001, studentName: '张伟', studentNo: '2021001', courseId: 1, courseName: '计算机导论', semester: '2024-2025-1', usualScore: 85, midtermScore: 78, finalScore: 88, totalScore: 84.1, gpa: 3.3, status: 'normal' },
  { id: 2, studentId: 2021002, studentName: '李娜', studentNo: '2021002', courseId: 1, courseName: '计算机导论', semester: '2024-2025-1', usualScore: 90, midtermScore: 85, finalScore: 92, totalScore: 89.5, gpa: 4.0, status: 'normal' },
  { id: 3, studentId: 2021003, studentName: '王强', studentNo: '2021003', courseId: 2, courseName: '数据结构', semester: '2024-2025-1', usualScore: 70, midtermScore: 65, finalScore: 72, totalScore: 69.6, gpa: 2.0, status: 'normal' },
  { id: 4, studentId: 2022001, studentName: '刘洋', studentNo: '2022001', courseId: 4, courseName: '经济学原理', semester: '2024-2025-1', usualScore: 88, midtermScore: 90, finalScore: 85, totalScore: 87.4, gpa: 3.7, status: 'normal' },
  { id: 5, studentId: 2023001, studentName: '赵雪', studentNo: '2023001', courseId: 1, courseName: '计算机导论', semester: '2024-2025-1', usualScore: 60, midtermScore: 55, finalScore: 58, totalScore: 57.5, gpa: 0, status: 'normal' }
]

export const useScoreStore = defineStore('score', () => {
  const scores = ref<Score[]>([])
  const weight = ref<ScoreWeight>({ ...DEFAULT_WEIGHT })

  function loadScores() {
    if (scores.value.length === 0) {
      const restored = restore<Score[]>(PERSIST_KEY, mockScores)
      scores.value = restored.map((s) => enrichScore(s, weight.value))
    }
  }

  function recalcAll() {
    scores.value = scores.value.map((s) => enrichScore(s, weight.value))
    persist(PERSIST_KEY, scores.value)
  }

  function addScore(s: Score) {
    scores.value.push(enrichScore(s, weight.value))
    persist(PERSIST_KEY, scores.value)
  }

  function updateScore(s: Score) {
    const idx = scores.value.findIndex((item) => item.id === s.id)
    if (idx !== -1) {
      scores.value[idx] = enrichScore(s, weight.value)
      persist(PERSIST_KEY, scores.value)
    }
  }

  function deleteScore(id: number) {
    const idx = scores.value.findIndex((item) => item.id === id)
    if (idx !== -1) {
      scores.value.splice(idx, 1)
      persist(PERSIST_KEY, scores.value)
    }
  }

  // 统计
  const stats = computed(() => {
    const totals = scores.value.map((s) => s.totalScore)
    const count = totals.length
    if (count === 0) return { avg: 0, max: 0, min: 0, passRate: 0 }
    const avg = Number((totals.reduce((a, b) => a + b, 0) / count).toFixed(1))
    const max = Math.max(...totals)
    const min = Math.min(...totals)
    const passCount = totals.filter((s) => s >= 60).length
    const passRate = Number(((passCount / count) * 100).toFixed(1))
    return { avg, max, min, passRate }
  })

  function getScoresByCourse(courseId: number): Score[] {
    return scores.value.filter((s) => s.courseId === courseId)
  }

  function getScoresByStudent(studentId: number): Score[] {
    return scores.value.filter((s) => s.studentId === studentId)
  }

  return {
    scores,
    weight,
    stats,
    loadScores,
    recalcAll,
    addScore,
    updateScore,
    deleteScore,
    getScoresByCourse,
    getScoresByStudent
  }
})
