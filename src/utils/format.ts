/**
 * 数值千分位格式化
 */
export function formatNumber(val: number): string {
  return val.toLocaleString('zh-CN')
}

/**
 * 日期格式化
 */
export function formatDate(date: Date | string | number, fmt = 'yyyy-MM-dd'): string {
  const d = new Date(date)
  const o: Record<string, number> = {
    'M+': d.getMonth() + 1,
    'd+': d.getDate(),
    'h+': d.getHours(),
    'm+': d.getMinutes(),
    's+': d.getSeconds()
  }
  if (/(y+)/.test(fmt)) {
    fmt = fmt.replace(RegExp.$1, String(d.getFullYear()).slice(4 - RegExp.$1.length))
  }
  for (const k in o) {
    if (new RegExp(`(${k})`).test(fmt)) {
      const v = o[k] < 10 ? `0${o[k]}` : o[k]
      fmt = fmt.replace(RegExp.$1, String(v).slice(0, RegExp.$1.length))
    }
  }
  return fmt
}
