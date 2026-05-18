<template>
  <v-chart class="chart-panel" :option="props.option" autoresize :style="{ height: props.height + 'px' }" />
</template>

<script setup lang="ts">
import VChart from 'vue-echarts'
import type { EChartsOption } from 'echarts/core'

interface Props {
  option: EChartsOption
  height?: number
}

const props = withDefaults(defineProps<Props>(), {
  height: 320
})
</script>

<style scoped lang="scss">
.chart-panel {
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
}
</style>
