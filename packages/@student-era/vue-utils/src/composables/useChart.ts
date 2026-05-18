import { ref, onMounted, onUnmounted, watch, type Ref } from 'vue'
import * as echarts from 'echarts/core'
import type { EChartsOption, ECharts } from 'echarts/core'

export function useChart(
  domRef: Ref<HTMLElement | null>,
  option: Ref<EChartsOption>,
  theme: string = 'default'
) {
  let chart: ECharts | null = null

  const initChart = () => {
    if (!domRef.value) return
    chart = echarts.init(domRef.value, theme)
    chart.setOption(option.value, true)
  }

  const handleResize = () => {
    chart?.resize()
  }

  onMounted(() => {
    initChart()
    window.addEventListener('resize', handleResize)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
    chart?.dispose()
    chart = null
  })

  watch(
    () => option.value,
    (newOpt) => {
      chart?.setOption(newOpt, true)
    },
    { deep: true }
  )

  return { chart }
}
