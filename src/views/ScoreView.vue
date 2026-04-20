<template>
  <div class="score-view">
    <!-- 统计卡片 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :xs="24" :sm="12" :md="6">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">平均分</div><div class="stat-value">{{ scoreStore.stats.avg }}</div></div></el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">最高分</div><div class="stat-value">{{ scoreStore.stats.max }}</div></div></el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">最低分</div><div class="stat-value">{{ scoreStore.stats.min }}</div></div></el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card shadow="hover"><div class="stat-item"><div class="stat-label">及格率</div><div class="stat-value">{{ scoreStore.stats.passRate }}%</div></div></el-card>
      </el-col>
    </el-row>

    <!-- 权重配置 + 筛选 -->
    <el-card shadow="never" class="filter-card">
      <div class="filter-bar">
        <div class="weight-config">
          <span class="filter-label">成绩权重：</span>
          <span>平时 {{ Math.round(scoreStore.weight.usual * 100) }}%</span>
          <el-slider v-model="usualWeight" :max="100" style="width: 120px; margin: 0 12px" @change="handleWeightChange" />
          <span>期中 {{ Math.round(scoreStore.weight.midterm * 100) }}%</span>
          <el-slider v-model="midtermWeight" :max="100" style="width: 120px; margin: 0 12px" @change="handleWeightChange" />
          <span>期末 {{ Math.round(scoreStore.weight.final * 100) }}%</span>
        </div>
        <div class="filter-actions">
          <el-select v-model="filterCourseId" placeholder="筛选课程" clearable style="width: 180px" @change="handleFilterChange">
            <el-option v-for="c in courseStore.courses" :key="c.id" :label="c.name" :value="c.id" />
          </el-select>
          <el-button type="success" plain @click="handleExport">导出Excel</el-button>
          <el-button v-permission="'score:enter'" type="primary" @click="handleAdd">录入成绩</el-button>
        </div>
      </div>
    </el-card>

    <!-- 成绩表格 -->
    <el-card shadow="never">
      <el-table :data="filteredScores" stripe border>
        <el-table-column prop="studentNo" label="学号" width="120" />
        <el-table-column prop="studentName" label="姓名" width="100" />
        <el-table-column prop="courseName" label="课程" />
        <el-table-column prop="semester" label="学期" />
        <el-table-column prop="usualScore" label="平时" width="90" sortable />
        <el-table-column prop="midtermScore" label="期中" width="90" sortable />
        <el-table-column prop="finalScore" label="期末" width="90" sortable />
        <el-table-column prop="totalScore" label="总评" width="100" sortable>
          <template #default="{ row }">
            <el-tag :type="row.totalScore >= 60 ? 'success' : 'danger'" size="small">{{ row.totalScore }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="gpa" label="绩点" width="80" sortable />
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button v-permission="'score:enter'" link type="primary" size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button v-permission="'score:audit'" link type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 成绩分布图 -->
    <el-row :gutter="16" class="chart-row">
      <el-col :xs="24" :lg="12">
        <el-card shadow="never"><ChartPanel :option="distributionOption" :height="320" /></el-card>
      </el-col>
      <el-col :xs="24" :lg="12">
        <el-card shadow="never"><ChartPanel :option="gpaOption" :height="320" /></el-card>
      </el-col>
    </el-row>

    <!-- 录入/编辑对话框 -->
    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑成绩' : '录入成绩'" width="480px" destroy-on-close>
      <el-form :model="form" label-width="90px">
        <el-form-item label="学生">
          <el-select v-model="form.studentId" style="width: 100%" :disabled="isEdit">
            <el-option v-for="s in studentStore.students" :key="s.id" :label="`${s.name} (${s.id})`" :value="s.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="课程">
          <el-select v-model="form.courseId" style="width: 100%" :disabled="isEdit">
            <el-option v-for="c in courseStore.courses" :key="c.id" :label="c.name" :value="c.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="平时成绩"><el-input-number v-model="form.usualScore" :min="0" :max="100" /></el-form-item>
        <el-form-item label="期中成绩"><el-input-number v-model="form.midtermScore" :min="0" :max="100" /></el-form-item>
        <el-form-item label="期末成绩"><el-input-number v-model="form.finalScore" :min="0" :max="100" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import ChartPanel from '@/components/ChartPanel.vue'
import { useScoreStore } from '@/stores/score'
import { useStudentStore } from '@/stores/student'
import { useCourseStore } from '@/stores/course'
import { exportToExcel } from '@/utils/export'
import type { Score } from '@/types/score'

const scoreStore = useScoreStore()
const studentStore = useStudentStore()
const courseStore = useCourseStore()

const dialogVisible = ref(false)
const isEdit = ref(false)
const filterCourseId = ref<number | ''>('')

const usualWeight = ref(30)
const midtermWeight = ref(20)

const defaultForm: Score = {
  id: 0, studentId: 0, studentName: '', studentNo: '',
  courseId: 0, courseName: '', semester: '2024-2025-1',
  usualScore: 0, midtermScore: 0, finalScore: 0, totalScore: 0, gpa: 0, status: 'normal'
}
const form = ref<Score>({ ...defaultForm })

onMounted(() => {
  scoreStore.loadScores()
  studentStore.loadStudents()
  courseStore.loadCourses()
})

const filteredScores = computed(() => {
  if (!filterCourseId.value) return scoreStore.scores
  return scoreStore.scores.filter((s) => s.courseId === filterCourseId.value)
})

watch(filteredScores, () => {
  updateChartOptions()
}, { immediate: true })

const distributionOption = ref({})
const gpaOption = ref({})

function updateChartOptions() {
  const data = filteredScores.value.map((s) => s.totalScore)
  const ranges = ['<60', '60-70', '70-80', '80-90', '90-100']
  const counts = [
    data.filter((s) => s < 60).length,
    data.filter((s) => s >= 60 && s < 70).length,
    data.filter((s) => s >= 70 && s < 80).length,
    data.filter((s) => s >= 80 && s < 90).length,
    data.filter((s) => s >= 90).length
  ]

  distributionOption.value = {
    title: { text: '成绩分布', left: 'center' },
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: ranges },
    yAxis: { type: 'value' },
    series: [{ data: counts, type: 'bar', barWidth: '50%', itemStyle: { borderRadius: [6, 6, 0, 0], color: '#409eff' } }]
  }

  const gpaCounts = [0, 0, 0, 0, 0]
  filteredScores.value.forEach((s) => {
    if (s.gpa >= 4) gpaCounts[4]++
    else if (s.gpa >= 3) gpaCounts[3]++
    else if (s.gpa >= 2) gpaCounts[2]++
    else if (s.gpa >= 1) gpaCounts[1]++
    else gpaCounts[0]++
  })

  gpaOption.value = {
    title: { text: '绩点分布', left: 'center' },
    tooltip: { trigger: 'item' },
    series: [{
      type: 'pie',
      radius: ['40%', '65%'],
      data: [
        { value: gpaCounts[0], name: '<1.0', itemStyle: { color: '#f56c6c' } },
        { value: gpaCounts[1], name: '1.0-1.9', itemStyle: { color: '#e6a23c' } },
        { value: gpaCounts[2], name: '2.0-2.9', itemStyle: { color: '#409eff' } },
        { value: gpaCounts[3], name: '3.0-3.9', itemStyle: { color: '#67c23a' } },
        { value: gpaCounts[4], name: '4.0', itemStyle: { color: '#9254de' } }
      ]
    }]
  }
}

function handleWeightChange() {
  const total = usualWeight.value + midtermWeight.value
  if (total > 100) {
    ElMessage.warning('权重总和不能超过 100%')
    return
  }
  scoreStore.weight.usual = usualWeight.value / 100
  scoreStore.weight.midterm = midtermWeight.value / 100
  scoreStore.weight.final = (100 - total) / 100
  scoreStore.recalcAll()
  updateChartOptions()
  ElMessage.success('权重已更新，成绩已重新计算')
}

function handleFilterChange() {
  updateChartOptions()
}

function handleAdd() {
  isEdit.value = false
  form.value = { ...defaultForm, id: Date.now() }
  dialogVisible.value = true
}

function handleEdit(row: Score) {
  isEdit.value = true
  form.value = { ...row }
  dialogVisible.value = true
}

function handleSubmit() {
  const s = studentStore.students.find((x) => x.id === form.value.studentId)
  const c = courseStore.courses.find((x) => x.id === form.value.courseId)
  form.value.studentName = s?.name ?? ''
  form.value.studentNo = String(s?.id ?? '')
  form.value.courseName = c?.name ?? ''
  form.value.semester = c?.semester ?? '2024-2025-1'

  if (isEdit.value) scoreStore.updateScore(form.value)
  else scoreStore.addScore(form.value)

  updateChartOptions()
  ElMessage.success(isEdit.value ? '编辑成功' : '录入成功')
  dialogVisible.value = false
}

function handleExport() {
  exportToExcel(filteredScores.value, '成绩信息表', {
    studentNo: '学号', studentName: '姓名', courseName: '课程', semester: '学期',
    usualScore: '平时', midtermScore: '期中', finalScore: '期末', totalScore: '总评', gpa: '绩点'
  })
}

function handleDelete(row: Score) {
  ElMessageBox.confirm(`确定删除该成绩记录吗？`, '提示', { type: 'warning' }).then(() => {
    scoreStore.deleteScore(row.id)
    updateChartOptions()
    ElMessage.success('删除成功')
  })
}
</script>

<style scoped lang="scss">
.score-view {
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

.filter-card {
  .filter-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
  }
  .weight-config {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #606266;
  }
  .filter-actions {
    display: flex;
    gap: 12px;
  }
}

.chart-row {
  margin-top: 8px;
}
</style>
