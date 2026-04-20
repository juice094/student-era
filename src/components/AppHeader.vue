<template>
  <header class="app-header">
    <div class="header-brand">
      <h1 class="header-title">教务大数据可视化平台</h1>
    </div>
    <nav class="header-nav">
      <a
        v-for="item in navItems"
        :key="item.path"
        href="javascript:;"
        :class="['nav-link', { active: currentPath === item.path }]"
        @click="go(item.path)"
      >
        {{ item.title }}
      </a>
    </nav>
    <div class="header-actions">
      <el-tag type="primary" effect="plain">Vue 3 + Vite</el-tag>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const currentPath = ref(route.path)

watch(() => route.path, (path) => {
  currentPath.value = path
  document.title = `${String(route.meta.title || '页面')} — 教务可视化系统`
})

const navItems = [
  { path: '/', title: '首页概览' },
  { path: '/student', title: '学生管理' },
  { path: '/about', title: '关于系统' }
]

function go(path: string) {
  console.log('[Nav] clicking:', path)
  router.push(path).catch((err) => {
    console.error('[Nav] router.push failed:', err)
  })
}
</script>

<style scoped lang="scss">
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 64px;
  background: #ffffff;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-title {
  font-size: 20px;
  font-weight: 700;
  color: #303133;
  margin: 0;
  background: linear-gradient(90deg, #409eff, #67c23a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.header-nav {
  display: flex;
  gap: 8px;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 8px;
  text-decoration: none;
  color: #606266;
  font-size: 15px;
  transition: all 0.2s ease;
  cursor: pointer;
  border: none;
  background: transparent;

  &:hover {
    background: #f5f7fa;
    color: #409eff;
  }

  &.active {
    background: #ecf5ff;
    color: #409eff;
    font-weight: 600;
  }
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>
