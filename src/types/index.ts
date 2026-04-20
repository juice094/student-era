export interface ApiResponse<T = unknown> {
  code: number
  message: string
  data: T
}

export interface Student {
  id: number
  name: string
  gender: '男' | '女'
  age: number
  major: string
  grade: string
  enrollmentYear: number
}

export interface ScoreDistribution {
  range: string
  count: number
}

export interface ChartData {
  xAxis: string[]
  series: number[]
}
