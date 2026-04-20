<template>
  <div class="home-view">
    <el-row :gutter="16" class="data-row">
      <el-col :xs="24" :sm="12" :md="6" v-for="card in summaryCards" :key="card.label">
        <DataCard v-bind="card" />
      </el-col>
    </el-row>

    <el-row :gutter="16" class="chart-row">
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>各院系学生人数分布</span>
              <el-tag size="small" type="info">柱状图</el-tag>
            </div>
          </template>
          <ChartPanel :option="majorOption" :height="340" />
        </el-card>
      </el-col>
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>学生性别比例</span>
              <el-tag size="small" type="info">饼图</el-tag>
            </div>
          </template>
          <ChartPanel :option="genderOption" :height="340" />
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="16" class="chart-row">
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>成绩分布统计</span>
              <el-tag size="small" type="info">柱状图</el-tag>
            </div>
          </template>
          <ChartPanel :option="scoreDistOption" :height="340" />
        </el-card>
      </el-col>
      <el-col :xs="24" :lg="12">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>课程类型占比</span>
              <el-tag size="small" type="info">饼图</el-tag>
            </div>
          </template>
          <ChartPanel :option="courseTypeOption" :height="340" />
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="16" class="chart-row">
      <el-col :span="24">
        <el-card shadow="never" class="chart-card">
          <template #header>
            <div class="card-header">
              <span>近五年招生趋势</span>
              <el-tag size="small" type="info">折线图</el-tag>
            </div>
          </template>
          <ChartPanel :option="enrollmentOption" :height="360" />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { UserFilled, Male, Female, School, Reading, TrendCharts } from '@element-plus/icons-vue'
import DataCard from '@/components/DataCard.vue'
import ChartPanel from '@/components/ChartPanel.vue'
import { useStudentStore } from '@/stores/student'
import { useCourseStore } from '@/stores/course'
import { useScoreStore } from '@/stores/score'

const studentStore = useStudentStore()
const courseStore = useCourseStore()
const scoreStore = useScoreStore()

onMounted(() => {
  studentStore.loadStudents()
  courseStore.loadCourses()
  scoreStore.loadScores()
})

const summaryCards = computed(() => [
  { icon: 'UserFilled', iconBg: '#409eff', label: '在校学生总数', value: studentStore.students.length || 12486, trend: 5.2 },
  { icon: 'Male', iconBg: '#67c23a', label: '男生人数', value: studentStore.students.filter((s) => s.gender === '男').length || 6820, trend: 3.1 },
  { icon: 'Female', iconBg: '#e6a23c', label: '女生人数', value: studentStore.students.filter((s) => s.gender === '女').length || 5666, trend: 7.8 },
  { icon: 'Reading', iconBg: '#f56c6c', label: '开设课程数', value: courseStore.courses.length || 42, trend: 2.4 }
])

const majorOption = computed(() => ({
  tooltip: { trigger: 'axis' },
  grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
  xAxis: { type: 'category', data: ['计算机', '电子信息', '经济管理', '机械工程', '土木工程', '外语', '艺术设计'] },
  yAxis: { type: 'value' },
  series: [
    {
      data: [2100, 1850, 2400, 1600, 1350, 980, 1206],
      type: 'bar',
      itemStyle: { borderRadius: [6, 6, 0, 0], color: '#409eff' }
    }
  ]
}))

const genderOption = computed(() => ({
  tooltip: { trigger: 'item' },
  legend: { bottom: '0%' },
  series: [
    {
      type: 'pie',
      radius: ['40%', '65%'],
      avoidLabelOverlap: false,
      itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2 },
      label: { show: true, formatter: '{b}: {d}%' },
      data: [
        { value: studentStore.students.filter((s) => s.gender === '男').length || 6820, name: '男生', itemStyle: { color: '#67c23a' } },
        { value: studentStore.students.filter((s) => s.gender === '女').length || 5666, name: '女生', itemStyle: { color: '#e6a23c' } }
      ]
    }
  ]
}))

const scoreDistOption = computed(() => {
  const scores = scoreStore.scores.map((s) => s.totalScore)
  return {
    tooltip: { trigger: 'axis' },
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'category', data: ['<60', '60-70', '70-80', '80-90', '90-100'] },
    yAxis: { type: 'value' },
    series: [{
      data: [
        scores.filter((s) => s < 60).length || 12,
        scores.filter((s) => s >= 60 && s < 70).length || 45,
        scores.filter((s) => s >= 70 && s < 80).length || 128,
        scores.filter((s) => s >= 80 && s < 90).length || 210,
        scores.filter((s) => s >= 90).length || 86
      ],
      type: 'bar',
      barWidth: '40%',
      itemStyle: {
        borderRadius: [6, 6, 0, 0],
        color: (params: any) => {
          const colors = ['#f56c6c', '#e6a23c', '#409eff', '#67c23a', '#9254de']
          return colors[params.dataIndex]
        }
      }
    }]
  }
})

const courseTypeOption = computed(() => {
  const courses = courseStore.courses
  const required = courses.filter((c) => c.type === '必修').length || 25
  const elective = courses.filter((c) => c.type === '选修').length || 12
  const general = courses.filter((c) => c.type === '通识').length || 5
  return {
    tooltip: { trigger: 'item' },
    legend: { bottom: '0%' },
    series: [{
      type: 'pie',
      radius: ['40%', '65%'],
      itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2 },
      label: { show: true, formatter: '{b}: {d}%' },
      data: [
        { value: required, name: '必修', itemStyle: { color: '#409eff' } },
        { value: elective, name: '选修', itemStyle: { color: '#67c23a' } },
        { value: general, name: '通识', itemStyle: { color: '#e6a23c' } }
      ]
    }]
  }
})

const enrollmentOption = computed(() => ({
  tooltip: { trigger: 'axis' },
  grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
  xAxis: { type: 'category', boundaryGap: false, data: ['2021', '2022', '2023', '2024', '2025'] },
  yAxis: { type: 'value' },
  series: [
    {
      data: [2100, 2280, 2450, 2600, 2756],
      type: 'line',
      smooth: true,
      areaStyle: { color: 'rgba(64, 158, 255, 0.15)' },
      lineStyle: { color: '#409eff', width: 3 },
      itemStyle: { color: '#409eff' }
    }
  ]
}))
</script>

<style scoped lang="scss">
.home-view {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.data-row {
  margin-bottom: 8px;
}

.chart-row {
  margin-bottom: 8px;
}

.chart-card {
  border-radius: 12px;
  margin-bottom: 16px;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
  font-size: 15px;
  color: #303133;
}
</style>
