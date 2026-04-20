import request from '../request'
import type { Student, ScoreDistribution, ApiResponse } from '@/types'

export function fetchStudentList(): Promise<ApiResponse<Student[]>> {
  return request.get('/students')
}

export function fetchScoreDistribution(): Promise<ApiResponse<ScoreDistribution[]>> {
  return request.get('/scores/distribution')
}
