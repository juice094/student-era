<template>
  <div class="evaluation-view">
    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>学生评教</span>
          <el-select v-model="filterCourseId" placeholder="选择课程" clearable style="width: 200px">
            <el-option v-for="c in courseStore.courses" :key="c.id" :label="c.name" :value="c.id" />
          </el-select>
        </div>
      </template>

      <el-table :data="filteredEvaluations" stripe border>
        <el-table-column prop="courseName" label="课程" />
        <el-table-column prop="teacherName" label="授课教师" width="120" />
        <el-table-column prop="semester" label="学期" />
        <el-table-column prop="avgScore" label="平均分" width="100" sortable>
          <template #default="{ row }">
            <el-rate v-model="row.avgScore" disabled show-score :max="5" />
          </template>
        </el-table-column>
        <el-table-column prop="participantCount" label="参评人数" width="100" />
        <el-table-column prop="totalCount" label="应评人数" width="100" />
        <el-table-column label="参评率" width="120">
          <template #default="{ row }">
            <el-progress :percentage="Math.round((row.participantCount / row.totalCount) * 100)" />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="{ row }">
            <el-button link type="primary" size="small" @click="showDetail(row)">查看详情</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 评教详情 -->
    <el-dialog v-model="detailVisible" title="评教详情" width="600px">
      <div v-if="currentEval">
        <h4>{{ currentEval.courseName }} — {{ currentEval.teacherName }}</h4>
        <el-divider />
        <div v-for="(item, idx) in currentEval.details" :key="idx" class="eval-item">
          <div class="eval-label">{{ item.label }}</div>
          <el-rate v-model="item.score" disabled show-score :max="5" />
          <div class="eval-bar">
            <el-progress :percentage="Math.round((item.score / 5) * 100)" :color="item.score >= 4 ? '#67c23a' : item.score >= 3 ? '#e6a23c' : '#f56c6c'" />
          </div>
        </div>
        <el-divider />
        <div class="eval-comment">
          <h5>学生留言精选</h5>
          <el-timeline>
            <el-timeline-item v-for="(c, i) in currentEval.comments" :key="i" :timestamp="c.time">
              {{ c.content }}
            </el-timeline-item>
          </el-timeline>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useCourseStore } from '@/stores/course'

const courseStore = useCourseStore()
const filterCourseId = ref<number | ''>('')
const detailVisible = ref(false)
const currentEval = ref<any>(null)

const evaluations = ref([
  {
    id: 1, courseId: 1, courseName: '计算机导论', teacherName: '王教授', semester: '2024-2025-1',
    avgScore: 4.5, participantCount: 85, totalCount: 100,
    details: [
      { label: '教学态度', score: 4.6 },
      { label: '教学内容', score: 4.4 },
      { label: '教学方法', score: 4.3 },
      { label: '师生互动', score: 4.5 },
      { label: '教学效果', score: 4.7 }
    ],
    comments: [
      { content: '王教授讲课非常生动，案例丰富，受益匪浅！', time: '2024-12-15' },
      { content: '课程节奏适中，课后答疑很耐心。', time: '2024-12-14' },
      { content: '希望能增加更多实践环节。', time: '2024-12-13' }
    ]
  },
  {
    id: 2, courseId: 2, courseName: '数据结构', teacherName: '王教授', semester: '2024-2025-1',
    avgScore: 4.2, participantCount: 78, totalCount: 100,
    details: [
      { label: '教学态度', score: 4.3 },
      { label: '教学内容', score: 4.5 },
      { label: '教学方法', score: 4.0 },
      { label: '师生互动', score: 4.1 },
      { label: '教学效果', score: 4.1 }
    ],
    comments: [
      { content: '课程内容很有深度，但作业量偏大。', time: '2024-12-15' },
      { content: '建议增加更多图解辅助理解。', time: '2024-12-14' }
    ]
  },
  {
    id: 3, courseId: 4, courseName: '经济学原理', teacherName: '张老师', semester: '2024-2025-1',
    avgScore: 4.7, participantCount: 120, totalCount: 150,
    details: [
      { label: '教学态度', score: 4.8 },
      { label: '教学内容', score: 4.6 },
      { label: '教学方法', score: 4.7 },
      { label: '师生互动', score: 4.8 },
      { label: '教学效果', score: 4.7 }
    ],
    comments: [
      { content: '张老师讲课非常有激情，课堂氛围很好！', time: '2024-12-15' },
      { content: '理论与实际结合得很好。', time: '2024-12-14' }
    ]
  }
])

onMounted(() => courseStore.loadCourses())

const filteredEvaluations = computed(() => {
  if (!filterCourseId.value) return evaluations.value
  return evaluations.value.filter((e) => e.courseId === filterCourseId.value)
})

function showDetail(row: any) {
  currentEval.value = row
  detailVisible.value = true
}
</script>

<style scoped lang="scss">
.evaluation-view {
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
.eval-item {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
  .eval-label {
    width: 100px;
    font-size: 14px;
    color: #606266;
  }
  .eval-bar {
    flex: 1;
  }
}
.eval-comment {
  h5 {
    margin: 0 0 12px;
    font-size: 15px;
    color: #303133;
  }
}
</style>
