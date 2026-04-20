export interface Course {
  id: number
  courseNo: string
  name: string
  credit: number
  hours: number
  type: '必修' | '选修' | '通识'
  collegeId: number
  collegeName: string
  teacherId?: number
  teacherName?: string
  semester: string
  maxStudents?: number
  description?: string
}
