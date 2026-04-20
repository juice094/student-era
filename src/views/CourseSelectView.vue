<template>
  <div class="course-select-view">
    <el-row :gutter="16" class="stat-row">
      <el-col :xs="24" :sm="12" :md="8">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">已选课程数</div><div class="stat-value">{{ courseSelectStore.selectedCount }}</div></div></el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">已获得学分</div><div class="stat-value">{{ courseSelectStore.totalCredits }}</div></div></el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">本学期上限</div><div class="stat-value">30</div></div></el-card>
      </el-col>
    </el-row>

    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>可选课程列表</span>
          <el-select v-model="filterSemester" placeholder="选择学期" style="width: 200px">
            <el-option v-for="s in dictStore.getDict('semester')" :key="s.value" :label="s.label" :value="s.value" />
          </el-select>
        </div>
      </template>

      <el-table :data="availableCourses" stripe border>
        <el-table-column prop="courseNo" label="课程号" width="100" />
        <el-table-column prop="name" label="课程名称" />
        <el-table-column prop="credit" label="学分" width="80" />
        <el-table-column prop="hours" label="学时" width="80" />
        <el-table-column prop="type" label="类型" width="100" />
        <el-table-column prop="teacherName" label="授课教师" width="120" />
        <el-table-column prop="maxStudents" label="容量" width="80" />
        <el-table-column label="已选/容量" width="120">
          <template #default="{ row }">
            <el-progress :percentage="Math.round((getSelectedCount(row.id) / (row.maxStudents || 100)) * 100)" :stroke-width="8" />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120" fixed="right">
          <template #default="{ row }">
            <el-button v-if="!isSelected(row.id)" type="primary" size="small" @click="handleSelect(row)">选课</el-button>
            <el-button v-else type="danger" size="small" @click="handleDrop(row)">退课</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-card shadow="never" class="my-course-card">
      <template #header>
        <div class="card-header"><span>我的已选课程</span></div>
      </template>
      <el-table :data="myCourses" stripe border>
        <el-table-column prop="courseNo" label="课程号" width="100" />
        <el-table-column prop="courseName" label="课程名称" />
        <el-table-column prop="credit" label="学分" width="80" />
        <el-table-column prop="teacherName" label="授课教师" width="120" />
        <el-table-column prop="selectTime" label="选课时间" />
        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" link size="small" @click="handleDropByRecord(row)">退课</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useCourseSelectStore } from '@/stores/courseSelect'
import { useCourseStore } from '@/stores/course'
import { useDictStore } from '@/stores/dict'
import { useUserStore } from '@/stores/user'
import type { Course } from '@/types/course'

const courseSelectStore = useCourseSelectStore()
const courseStore = useCourseStore()
const dictStore = useDictStore()
const userStore = useUserStore()

const filterSemester = ref('2024-2025-1')

onMounted(() => {
  courseSelectStore.loadRecords()
  courseStore.loadCourses()
})

const availableCourses = computed(() => {
  return courseStore.courses.filter((c) => c.semester === filterSemester.value)
})

const myCourses = computed(() => {
  if (!userStore.userInfo) return []
  return courseSelectStore.getMyCourses(userStore.userInfo.id)
})

function isSelected(courseId: number): boolean {
  if (!userStore.userInfo) return false
  return courseSelectStore.records.some(
    (r) => r.studentId === userStore.userInfo!.id && r.courseId === courseId && r.status === 'selected'
  )
}

function getSelectedCount(courseId: number): number {
  return courseSelectStore.records.filter((r) => r.courseId === courseId && r.status === 'selected').length
}

function handleSelect(course: Course) {
  if (!userStore.userInfo) return
  if (courseSelectStore.totalCredits + course.credit > 30) {
    ElMessage.warning('超出本学期学分上限（30学分）')
    return
  }
  const record = {
    id: Date.now(),
    studentId: userStore.userInfo.id,
    studentName: userStore.userInfo.realName,
    courseId: course.id,
    courseName: course.name,
    courseNo: course.courseNo,
    credit: course.credit,
    teacherName: course.teacherName || '',
    semester: course.semester,
    status: 'selected' as const,
    selectTime: new Date().toLocaleString()
  }
  courseSelectStore.selectCourse(record)
  ElMessage.success(`成功选修「${course.name}」`)
}

function handleDrop(course: Course) {
  const record = courseSelectStore.records.find(
    (r) => r.studentId === userStore.userInfo?.id && r.courseId === course.id && r.status === 'selected'
  )
  if (record) handleDropByRecord(record)
}

function handleDropByRecord(record: any) {
  ElMessageBox.confirm(`确定退选「${record.courseName}」吗？`, '提示', { type: 'warning' }).then(() => {
    courseSelectStore.dropCourse(record.id)
    ElMessage.success('退课成功')
  })
}
</script>

<style scoped lang="scss">
.course-select-view {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.stat-row {
  margin-bottom: 4px;
}
.stat-item {
  text-align: center;
  .stat-label {
    font-size: 14px;
    color: #909399;
    margin-bottom: 8px;
  }
  .stat-value {
    font-size: 28px;
    font-weight: 700;
    color: #303133;
  }
}
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
  font-size: 15px;
}
.my-course-card {
  margin-top: 8px;
}
</style>
