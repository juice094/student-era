<template>
  <div class="schedule-view">
    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>课程排课</span>
          <el-button type="primary" @click="dialogVisible = true">新增排课</el-button>
        </div>
      </template>

      <el-table :data="schedules" stripe border>
        <el-table-column prop="courseName" label="课程" />
        <el-table-column prop="teacherName" label="教师" width="120" />
        <el-table-column prop="classroom" label="教室" width="120" />
        <el-table-column prop="weekday" label="星期" width="100" />
        <el-table-column prop="timeSlot" label="时间段" width="150" />
        <el-table-column prop="weeks" label="上课周次" />
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button link type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 冲突检测提示 -->
    <el-card v-if="conflicts.length > 0" shadow="never" class="conflict-card">
      <template #header>
        <div class="card-header" style="color: #f56c6c;">
          <el-icon><Warning /></el-icon>
          <span>排课冲突检测（{{ conflicts.length }} 项）</span>
        </div>
      </template>
      <el-alert
        v-for="(c, idx) in conflicts"
        :key="idx"
        :title="c"
        type="error"
        :closable="false"
        style="margin-bottom: 8px"
      />
    </el-card>

    <!-- 排课对话框 -->
    <el-dialog v-model="dialogVisible" title="新增排课" width="500px" destroy-on-close>
      <el-form :model="form" label-width="90px">
        <el-form-item label="课程">
          <el-select v-model="form.courseId" style="width: 100%" @change="onCourseChange">
            <el-option v-for="c in courseStore.courses" :key="c.id" :label="`${c.name} (${c.teacherName})`" :value="c.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="教室">
          <el-select v-model="form.classroom" style="width: 100%">
            <el-option v-for="r in classrooms" :key="r" :label="r" :value="r" />
          </el-select>
        </el-form-item>
        <el-form-item label="星期">
          <el-select v-model="form.weekday" style="width: 100%">
            <el-option v-for="d in weekdays" :key="d.value" :label="d.label" :value="d.value" />
          </el-select>
        </el-form-item>
        <el-form-item label="时间段">
          <el-select v-model="form.timeSlot" style="width: 100%">
            <el-option v-for="t in timeSlots" :key="t" :label="t" :value="t" />
          </el-select>
        </el-form-item>
        <el-form-item label="上课周次">
          <el-input v-model="form.weeks" placeholder="例如: 1-16" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Warning } from '@element-plus/icons-vue'
import { useCourseStore } from '@/stores/course'

const courseStore = useCourseStore()
const dialogVisible = ref(false)

interface Schedule {
  id: number
  courseId: number
  courseName: string
  teacherName: string
  classroom: string
  weekday: string
  timeSlot: string
  weeks: string
}

const schedules = ref<Schedule[]>([
  { id: 1, courseId: 1, courseName: '计算机导论', teacherName: '王教授', classroom: 'A101', weekday: '周一', timeSlot: '08:00-09:40', weeks: '1-16' },
  { id: 2, courseId: 2, courseName: '数据结构', teacherName: '王教授', classroom: 'A102', weekday: '周三', timeSlot: '10:00-11:40', weeks: '1-16' },
  { id: 3, courseId: 4, courseName: '经济学原理', teacherName: '张老师', classroom: 'B201', weekday: '周二', timeSlot: '14:00-15:40', weeks: '1-16' }
])

const classrooms = ['A101', 'A102', 'A103', 'B201', 'B202', 'C301', 'C302', 'D401']
const weekdays = [
  { label: '周一', value: '周一' },
  { label: '周二', value: '周二' },
  { label: '周三', value: '周三' },
  { label: '周四', value: '周四' },
  { label: '周五', value: '周五' }
]
const timeSlots = ['08:00-09:40', '10:00-11:40', '14:00-15:40', '16:00-17:40', '19:00-20:40']

const form = ref({
  id: 0, courseId: 0, courseName: '', teacherName: '', classroom: '', weekday: '', timeSlot: '', weeks: '1-16'
})

onMounted(() => courseStore.loadCourses())

const conflicts = computed(() => {
  const list: string[] = []
  for (let i = 0; i < schedules.value.length; i++) {
    for (let j = i + 1; j < schedules.value.length; j++) {
      const a = schedules.value[i]
      const b = schedules.value[j]
      if (a.weekday === b.weekday && a.timeSlot === b.timeSlot && a.classroom === b.classroom) {
        list.push(`教室冲突：${a.weekday} ${a.timeSlot}，${a.courseName} 与 ${b.courseName} 都安排在 ${a.classroom}`)
      }
      if (a.weekday === b.weekday && a.timeSlot === b.timeSlot && a.teacherName === b.teacherName) {
        list.push(`教师冲突：${a.weekday} ${a.timeSlot}，${a.teacherName} 同时需要讲授 ${a.courseName} 与 ${b.courseName}`)
      }
    }
  }
  return list
})

function onCourseChange(courseId: number) {
  const c = courseStore.courses.find((x) => x.id === courseId)
  if (c) {
    form.value.courseName = c.name
    form.value.teacherName = c.teacherName || ''
  }
}

function handleEdit(row: Schedule) {
  form.value = { ...row }
  dialogVisible.value = true
}

function handleSubmit() {
  if (form.value.id) {
    const idx = schedules.value.findIndex((s) => s.id === form.value.id)
    if (idx !== -1) schedules.value[idx] = { ...form.value }
  } else {
    schedules.value.push({ ...form.value, id: Date.now() })
  }
  ElMessage.success('保存成功')
  dialogVisible.value = false
}

function handleDelete(row: Schedule) {
  ElMessageBox.confirm(`确定删除「${row.courseName}」的排课吗？`, '提示', { type: 'warning' }).then(() => {
    const idx = schedules.value.findIndex((s) => s.id === row.id)
    if (idx !== -1) schedules.value.splice(idx, 1)
    ElMessage.success('删除成功')
  })
}
</script>

<style scoped lang="scss">
.schedule-view {
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
.conflict-card {
  :deep(.el-card__header) {
    background: #fef0f0;
  }
}
</style>
