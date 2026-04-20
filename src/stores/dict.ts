import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface DictItem {
  label: string
  value: string | number
}

export interface DictGroup {
  code: string
  name: string
  items: DictItem[]
}

export const useDictStore = defineStore('dict', () => {
  const dicts = ref<Record<string, DictItem[]>>({
    college: [
      { label: '信息工程学院', value: 1 },
      { label: '经济管理学院', value: 2 },
      { label: '机械工程学院', value: 3 },
      { label: '土木工程学院', value: 4 },
      { label: '艺术设计学院', value: 5 },
      { label: '外国语学院', value: 6 }
    ],
    major: [
      { label: '计算机科学与技术', value: '计算机科学与技术' },
      { label: '软件工程', value: '软件工程' },
      { label: '电子信息工程', value: '电子信息工程' },
      { label: '经济管理', value: '经济管理' },
      { label: '机械工程', value: '机械工程' },
      { label: '土木工程', value: '土木工程' },
      { label: '艺术设计', value: '艺术设计' },
      { label: '外语', value: '外语' }
    ],
    grade: [
      { label: '大一', value: '大一' },
      { label: '大二', value: '大二' },
      { label: '大三', value: '大三' },
      { label: '大四', value: '大四' }
    ],
    gender: [
      { label: '男', value: '男' },
      { label: '女', value: '女' }
    ],
    courseType: [
      { label: '必修', value: '必修' },
      { label: '选修', value: '选修' },
      { label: '通识', value: '通识' }
    ],
    semester: [
      { label: '2024-2025学年 第一学期', value: '2024-2025-1' },
      { label: '2024-2025学年 第二学期', value: '2024-2025-2' },
      { label: '2025-2026学年 第一学期', value: '2025-2026-1' },
      { label: '2025-2026学年 第二学期', value: '2025-2026-2' }
    ]
  })

  function getDict(code: string): DictItem[] {
    return dicts.value[code] ?? []
  }

  function getLabel(code: string, value: string | number): string {
    const item = dicts.value[code]?.find((d) => d.value === value)
    return item?.label ?? String(value)
  }

  return { dicts, getDict, getLabel }
})
