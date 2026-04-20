import type { Directive } from 'vue'
import { useUserStore } from '@/stores/user'

export const permissionDirective: Directive = {
  mounted(el, binding) {
    const userStore = useUserStore()
    const code = binding.value as string
    if (!userStore.checkButton(code)) {
      el.parentNode?.removeChild(el)
    }
  }
}
