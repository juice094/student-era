<template>
  <div class="course-view">
    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>课程信息列表</span>
          <div>
            <el-upload :auto-upload="false" :show-file-list="false" @change="handleImport" style="display:inline-block; margin-right:8px">
              <el-button type="warning" plain>导入Excel</el-button>
            </el-upload>
            <el-button type="success" plain @click="handleExport">导出Excel</el-button>
            <el-button v-permission="'course:add'" type="primary" @click="handleAdd">新增课程</el-button>
          </div>
        </div>
      </template>

      <el-table :data="courseStore.courses" stripe border>
        <el-table-column prop="courseNo" label="课程号" width="100" />
        <el-table-column prop="name" label="课程名称" />
        <el-table-column prop="credit" label="学分" width="80" />
        <el-table-column prop="hours" label="学时" width="80" />
        <el-table-column prop="type" label="类型" width="100">
          <template #default="{ row }">
            <el-tag :type="row.type === '必修' ? 'primary' : row.type === '选修' ? 'success' : 'info'" size="small">{{ row.type }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="collegeName" label="开课学院" />
        <el-table-column prop="teacherName" label="授课教师" width="120" />
        <el-table-column prop="semester" label="学期" />
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button v-permission="'course:edit'" link type="primary" size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button v-permission="'course:delete'" link type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑课程' : '新增课程'" width="520px" destroy-on-close>
      <el-form :model="form" label-width="100px">
        <el-form-item label="课程号"><el-input v-model="form.courseNo" :disabled="isEdit" /></el-form-item>
        <el-form-item label="课程名称"><el-input v-model="form.name" /></el-form-item>
        <el-form-item label="学分"><el-input-number v-model="form.credit" :min="0.5" :max="10" :step="0.5" /></el-form-item>
        <el-form-item label="学时"><el-input-number v-model="form.hours" :min="8" :max="128" :step="8" /></el-form-item>
        <el-form-item label="课程类型">
          <el-select v-model="form.type" style="width: 100%"><el-option label="必修" value="必修" /><el-option label="选修" value="选修" /><el-option label="通识" value="通识" /></el-select>
        </el-form-item>
        <el-form-item label="开课学院">
          <el-select v-model="form.collegeId" style="width: 100%"><el-option v-for="c in dictStore.getDict('college')" :key="c.value" :label="c.label" :value="c.value" /></el-select>
        </el-form-item>
        <el-form-item label="授课教师">
          <el-select v-model="form.teacherId" style="width: 100%"><el-option v-for="t in teacherStore.teachers" :key="t.id" :label="t.name" :value="t.id" /></el-select>
        </el-form-item>
        <el-form-item label="学期">
          <el-select v-model="form.semester" style="width: 100%"><el-option v-for="s in dictStore.getDict('semester')" :key="s.value" :label="s.label" :value="s.value" /></el-select>
        </el-form-item>
        <el-form-item label="容量"><el-input-number v-model="form.maxStudents" :min="1" :max="500" /></el-form-item>
        <el-form-item label="课程简介"><el-input v-model="form.description" type="textarea" :rows="2" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useCourseStore } from '@/stores/course'
import { useTeacherStore } from '@/stores/teacher'
import { useDictStore } from '@/stores/dict'
import { exportToExcel, readExcelFile } from '@/utils/export'
import type { Course } from '@/types/course'

const courseStore = useCourseStore()
const teacherStore = useTeacherStore()
const dictStore = useDictStore()
const dialogVisible = ref(false)
const isEdit = ref(false)

const defaultForm: Course = {
  id: 0, courseNo: '', name: '', credit: 2, hours: 32, type: '必修',
  collegeId: 1, collegeName: '', teacherId: undefined, teacherName: '',
  semester: '2024-2025-1', maxStudents: 100, description: ''
}
const form = ref<Course>({ ...defaultForm })

onMounted(() => {
  courseStore.loadCourses()
  teacherStore.loadTeachers()
})

function handleAdd() {
  isEdit.value = false
  form.value = { ...defaultForm, id: Date.now() }
  dialogVisible.value = true
}

function handleEdit(row: Course) {
  isEdit.value = true
  form.value = { ...row }
  dialogVisible.value = true
}

function handleSubmit() {
  const college = dictStore.getDict('college').find((c) => c.value === form.value.collegeId)
  const teacher = teacherStore.teachers.find((t) => t.id === form.value.teacherId)
  form.value.collegeName = college?.label ?? ''
  form.value.teacherName = teacher?.name ?? ''

  if (isEdit.value) courseStore.updateCourse(form.value)
  else courseStore.addCourse(form.value)

  ElMessage.success(isEdit.value ? '编辑成功' : '新增成功')
  dialogVisible.value = false
}

function handleExport() {
  exportToExcel(courseStore.courses, '课程信息表', {
    courseNo: '课程号', name: '课程名称', credit: '学分', hours: '学时',
    type: '类型', collegeName: '开课学院', teacherName: '授课教师', semester: '学期'
  })
}

async function handleImport(file: any) {
  try {
    const rawFile = file.raw
    const data = await readExcelFile(rawFile)
    let count = 0
    for (const row of data) {
      const courseNo = String(row['课程号'] || row['courseNo'] || '')
      if (!courseNo) continue
      const exists = courseStore.courses.find((c) => c.courseNo === courseNo)
      const course: Course = {
        id: exists ? exists.id : Date.now() + count,
        courseNo,
        name: String(row['课程名称'] || row['name'] || ''),
        credit: Number(row['学分'] || row['credit'] || 2),
        hours: Number(row['学时'] || row['hours'] || 32),
        type: String(row['类型'] || row['type'] || '必修') as any,
        collegeId: 1,
        collegeName: String(row['开课学院'] || row['collegeName'] || ''),
        teacherName: String(row['授课教师'] || row['teacherName'] || ''),
        semester: String(row['学期'] || row['semester'] || '2024-2025-1'),
        maxStudents: Number(row['容量'] || row['maxStudents'] || 100),
        description: ''
      }
      if (exists) courseStore.updateCourse(course)
      else { courseStore.addCourse(course); count++ }
    }
    ElMessage.success(`导入成功，新增 ${count} 条课程`)
  } catch (err) {
    ElMessage.error('导入失败，请检查 Excel 格式')
  }
}

function handleDelete(row: Course) {
  ElMessageBox.confirm(`确定删除课程 "${row.name}" 吗？`, '提示', { type: 'warning' }).then(() => {
    courseStore.deleteCourse(row.id)
    ElMessage.success('删除成功')
  })
}
</script>

<style scoped lang="scss">
.course-view {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
  font-size: 15px;
}
</style>
