<template>
  <div class="student-view">
    <el-card shadow="never" class="table-card">
      <template #header>
        <div class="card-header">
          <span>学生信息列表</span>
          <el-button type="primary" @click="handleAdd">新增学生</el-button>
        </div>
      </template>

      <el-table :data="studentStore.students" stripe border>
        <el-table-column prop="id" label="学号" width="100" />
        <el-table-column prop="name" label="姓名" width="120" />
        <el-table-column prop="gender" label="性别" width="80" />
        <el-table-column prop="age" label="年龄" width="80" />
        <el-table-column prop="major" label="专业" />
        <el-table-column prop="grade" label="年级" width="100" />
        <el-table-column prop="enrollmentYear" label="入学年份" width="120" />
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button link type="primary" size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button link type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-row :gutter="16" class="chart-row">
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>成绩分布统计</span>
              <el-tag size="small" type="info">柱状图</el-tag>
            </div>
          </template>
          <ChartPanel :option="scoreOption" :height="340" />
        </el-card>
      </el-col>
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>专业人数占比</span>
              <el-tag size="small" type="info">饼图</el-tag>
            </div>
          </template>
          <ChartPanel :option="majorPieOption" :height="340" />
        </el-card>
      </el-col>
    </el-row>

    <!-- 新增/编辑共用表单对话框 -->
    <StudentFormDialog
      v-model:visible="dialogVisible"
      :data="editingStudent"
      @submit="handleFormSubmit"
    />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, h } from 'vue'
import { ElMessageBox, ElNotification } from 'element-plus'
import ChartPanel from '@/components/ChartPanel.vue'
import StudentFormDialog from '@/components/StudentFormDialog.vue'
import { useStudentStore } from '@/stores/student'
import type { Student } from '@/types'

const studentStore = useStudentStore()
const dialogVisible = ref(false)
const editingStudent = ref<Student | null>(null)

// 删除回溯：记录最后删除的数据和位置
const lastDeleted = ref<{ item: Student; index: number } | null>(null)

const mockStudents: Student[] = [
  { id: 2021001, name: '张伟', gender: '男', age: 21, major: '计算机科学与技术', grade: '大三', enrollmentYear: 2021 },
  { id: 2021002, name: '李娜', gender: '女', age: 20, major: '软件工程', grade: '大三', enrollmentYear: 2021 },
  { id: 2021003, name: '王强', gender: '男', age: 22, major: '电子信息工程', grade: '大四', enrollmentYear: 2020 },
  { id: 2022001, name: '刘洋', gender: '女', age: 20, major: '经济管理', grade: '大二', enrollmentYear: 2022 },
  { id: 2022002, name: '陈明', gender: '男', age: 19, major: '机械工程', grade: '大二', enrollmentYear: 2022 },
  { id: 2023001, name: '赵雪', gender: '女', age: 18, major: '土木工程', grade: '大一', enrollmentYear: 2023 },
  { id: 2023002, name: '孙涛', gender: '男', age: 19, major: '艺术设计', grade: '大一', enrollmentYear: 2023 },
  { id: 2021004, name: '周敏', gender: '女', age: 21, major: '外语', grade: '大三', enrollmentYear: 2021 },
  { id: 2020001, name: '吴磊', gender: '男', age: 23, major: '计算机科学与技术', grade: '大四', enrollmentYear: 2020 },
  { id: 2022003, name: '郑丽', gender: '女', age: 20, major: '软件工程', grade: '大二', enrollmentYear: 2022 }
]

onMounted(() => {
  if (studentStore.students.length === 0) {
    studentStore.students = mockStudents
  }
})

const scoreOption = computed(() => ({
  tooltip: { trigger: 'axis' },
  grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
  xAxis: { type: 'category', data: ['<60', '60-70', '70-80', '80-90', '90-100'] },
  yAxis: { type: 'value' },
  series: [
    {
      data: [12, 45, 128, 210, 86],
      type: 'bar',
      barWidth: '40%',
      itemStyle: {
        borderRadius: [6, 6, 0, 0],
        color: (params: any) => {
          const colors = ['#f56c6c', '#e6a23c', '#409eff', '#67c23a', '#9254de']
          return colors[params.dataIndex]
        }
      }
    }
  ]
}))

const majorPieOption = computed(() => ({
  tooltip: { trigger: 'item' },
  legend: { orient: 'vertical', left: 'left' },
  series: [
    {
      type: 'pie',
      radius: '60%',
      data: [
        { value: 350, name: '计算机科学与技术' },
        { value: 280, name: '软件工程' },
        { value: 220, name: '电子信息工程' },
        { value: 190, name: '经济管理' },
        { value: 160, name: '机械工程' },
        { value: 140, name: '土木工程' },
        { value: 120, name: '艺术设计' },
        { value: 110, name: '外语' }
      ],
      emphasis: {
        itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' }
      }
    }
  ]
}))

function handleAdd() {
  editingStudent.value = null
  dialogVisible.value = true
}

function handleEdit(row: Student) {
  editingStudent.value = row
  dialogVisible.value = true
}

function handleFormSubmit(data: Student) {
  if (editingStudent.value) {
    // 编辑模式：替换原有数据
    const index = studentStore.students.findIndex((s) => s.id === data.id)
    if (index !== -1) {
      studentStore.students[index] = { ...data }
    }
  } else {
    // 新增模式：检查学号是否重复
    const exists = studentStore.students.some((s) => s.id === data.id)
    if (exists) {
      ElMessageBox.alert('该学号已存在', '提示', { type: 'warning' })
      return
    }
    studentStore.students.push({ ...data })
  }
}

function handleDelete(row: Student) {
  ElMessageBox.confirm(`确定删除学生 "${row.name}" 吗？`, '提示', { type: 'warning' }).then(() => {
    const index = studentStore.students.findIndex((s) => s.id === row.id)
    if (index === -1) return

    // 记录删除前的状态，用于回溯
    lastDeleted.value = { item: { ...row }, index }

    studentStore.students.splice(index, 1)

    // 显示可撤销的通知
    ElNotification({
      title: '删除成功',
      type: 'success',
      duration: 8000,
      message: h('div', { style: 'display:flex;align-items:center;gap:12px' }, [
        h('span', `已删除学生 "${row.name}"`),
        h(
          'button',
          {
            style: 'color:#409eff;cursor:pointer;background:none;border:none;padding:0;font-size:13px;text-decoration:underline;',
            onClick: () => {
              if (lastDeleted.value) {
                const { item, index: idx } = lastDeleted.value
                studentStore.students.splice(idx, 0, item)
                lastDeleted.value = null
                ElNotification({ title: '已撤销', message: `恢复了学生 "${item.name}"`, type: 'info', duration: 3000 })
              }
            }
          },
          '撤销删除'
        )
      ])
    })
  })
}
</script>

<style scoped lang="scss">
.student-view {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.table-card {
  border-radius: 12px;
}

.chart-card {
  border-radius: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
  font-size: 15px;
  color: #303133;
}

.chart-row {
  margin-top: 8px;
}
</style>
