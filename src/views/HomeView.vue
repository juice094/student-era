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
import { computed } from 'vue'
import { UserFilled, Male, Female, School } from '@element-plus/icons-vue'
import DataCard from '@/components/DataCard.vue'
import ChartPanel from '@/components/ChartPanel.vue'

const summaryCards = [
  { icon: 'UserFilled', iconBg: '#409eff', label: '在校学生总数', value: '12,486', trend: 5.2 },
  { icon: 'Male', iconBg: '#67c23a', label: '男生人数', value: '6,820', trend: 3.1 },
  { icon: 'Female', iconBg: '#e6a23c', label: '女生人数', value: '5,666', trend: 7.8 },
  { icon: 'School', iconBg: '#f56c6c', label: '开设专业数', value: '42', trend: 2.4 }
]

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
        { value: 6820, name: '男生', itemStyle: { color: '#67c23a' } },
        { value: 5666, name: '女生', itemStyle: { color: '#e6a23c' } }
      ]
    }
  ]
}))

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
