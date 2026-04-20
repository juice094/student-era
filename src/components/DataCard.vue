<template>
  <el-card class="data-card" shadow="hover">
    <div class="card-body">
      <div class="card-icon" :style="{ background: props.iconBg }">
        <el-icon size="28" color="#fff">
          <component :is="props.icon" />
        </el-icon>
      </div>
      <div class="card-info">
        <div class="card-label">{{ props.label }}</div>
        <div class="card-value">{{ props.value }}</div>
        <div v-if="props.trend" class="card-trend" :class="props.trend > 0 ? 'up' : 'down'">
          {{ props.trend > 0 ? '↑' : '↓' }} {{ Math.abs(props.trend) }}%
        </div>
      </div>
    </div>
  </el-card>
</template>

<script setup lang="ts">
interface Props {
  icon: string
  iconBg: string
  label: string
  value: string | number
  trend?: number
}

const props = defineProps<Props>()
</script>

<style scoped lang="scss">
.data-card {
  border-radius: 12px;
  transition: transform 0.2s ease;

  &:hover {
    transform: translateY(-4px);
  }
}

.card-body {
  display: flex;
  align-items: center;
  gap: 16px;
}

.card-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-label {
  font-size: 14px;
  color: #909399;
  margin-bottom: 4px;
}

.card-value {
  font-size: 26px;
  font-weight: 700;
  color: #303133;
}

.card-trend {
  font-size: 13px;
  margin-top: 4px;

  &.up {
    color: #67c23a;
  }

  &.down {
    color: #f56c6c;
  }
}
</style>
