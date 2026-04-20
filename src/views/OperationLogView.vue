<template>
  <div class="log-view">
    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>操作日志</span>
          <div class="filter-bar">
            <el-input v-model="filterUser" placeholder="搜索用户" clearable style="width: 160px" />
            <el-select v-model="filterModule" placeholder="操作模块" clearable style="width: 140px">
              <el-option label="学生管理" value="学生管理" />
              <el-option label="教师管理" value="教师管理" />
              <el-option label="课程管理" value="课程管理" />
              <el-option label="成绩管理" value="成绩管理" />
              <el-option label="选课系统" value="选课系统" />
              <el-option label="系统管理" value="系统管理" />
            </el-select>
            <el-select v-model="filterStatus" placeholder="状态" clearable style="width: 100px">
              <el-option label="成功" value="success" />
              <el-option label="失败" value="fail" />
            </el-select>
          </div>
        </div>
      </template>

      <el-table :data="filteredLogs" stripe border>
        <el-table-column prop="id" label="ID" width="60" />
        <el-table-column prop="time" label="操作时间" width="180" />
        <el-table-column prop="realName" label="操作人" width="120" />
        <el-table-column prop="role" label="角色" width="100">
          <template #default="{ row }">
            <el-tag size="small" :type="row.role === 'admin' ? 'danger' : row.role === 'teacher' ? 'warning' : 'success'">{{ row.role }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="module" label="模块" width="120" />
        <el-table-column prop="action" label="操作类型" width="120" />
        <el-table-column prop="detail" label="详情" show-overflow-tooltip />
        <el-table-column prop="ip" label="IP地址" width="140" />
        <el-table-column prop="status" label="状态" width="80">
          <template #default="{ row }">
            <el-tag size="small" :type="row.status === 'success' ? 'success' : 'danger'">{{ row.status === 'success' ? '成功' : '失败' }}</el-tag>
          </template>
        </el-table-column>
      </el-table>

      <div class="pagination-bar">
        <el-pagination background layout="prev, pager, next" :total="filteredLogs.length" :page-size="10" />
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useLogStore } from '@/stores/log'

const logStore = useLogStore()

const filterUser = ref('')
const filterModule = ref('')
const filterStatus = ref('')

onMounted(() => logStore.loadLogs())

const filteredLogs = computed(() => {
  return logStore.logs.filter((log) => {
    if (filterUser.value && !log.realName.includes(filterUser.value) && !log.username.includes(filterUser.value)) return false
    if (filterModule.value && log.module !== filterModule.value) return false
    if (filterStatus.value && log.status !== filterStatus.value) return false
    return true
  })
})
</script>

<style scoped lang="scss">
.log-view {
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
.filter-bar {
  display: flex;
  gap: 12px;
}
.pagination-bar {
  display: flex;
  justify-content: flex-end;
  margin-top: 16px;
}
</style>
