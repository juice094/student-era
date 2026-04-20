export interface Score {
  id: number
  studentId: number
  studentName: string
  studentNo: string
  courseId: number
  courseName: string
  semester: string
  usualScore: number
  midtermScore: number
  finalScore: number
  totalScore: number
  gpa: number
  status: 'normal' | 'makeup' | 'retake'
}

export interface ScoreWeight {
  usual: number
  midterm: number
  final: number
}

export const DEFAULT_WEIGHT: ScoreWeight = {
  usual: 0.3,
  midterm: 0.2,
  final: 0.5
}
