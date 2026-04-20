export interface Teacher {
  id: number
  teacherNo: string
  name: string
  gender: '男' | '女'
  age: number
  title: string
  collegeId: number
  collegeName: string
  phone: string
  email: string
  courses?: string[]
}
