<template>
  <div class="about-view">
    <el-card shadow="never" class="about-card">
      <template #header>
        <div class="about-header">
          <el-icon size="24" color="#409eff"><InfoFilled /></el-icon>
          <span>关于本系统</span>
        </div>
      </template>

      <el-descriptions title="项目信息" :column="1" border>
        <el-descriptions-item label="项目名称">教务大数据可视化平台</el-descriptions-item>
        <el-descriptions-item label="课程名称">《大数据可视化》课程设计</el-descriptions-item>
        <el-descriptions-item label="技术栈">
          <el-space wrap>
            <el-tag>Vue 3.5</el-tag>
            <el-tag type="success">Vite 6</el-tag>
            <el-tag type="warning">TypeScript</el-tag>
            <el-tag type="danger">Element Plus</el-tag>
            <el-tag type="info">ECharts 5</el-tag>
            <el-tag>Pinia</el-tag>
            <el-tag type="success">Vue Router 4</el-tag>
          </el-space>
        </el-descriptions-item>
        <el-descriptions-item label="工程特性">
          <ul class="feature-list">
            <li>基于 <strong>Vite</strong> 的极速开发与构建体验（冷启动 &lt; 300ms）</li>
            <li>基于 <strong>Composition API</strong> 的逻辑复用与类型安全</li>
            <li>基于 <strong>Pinia</strong> 的极简状态管理</li>
            <li>基于 <strong>ECharts 5</strong> 的按需引入与封装，减小打包体积</li>
            <li>基于 <strong>Element Plus</strong> 的企业级 UI 组件</li>
            <li>基于 <strong>ESLint 9 Flat Config</strong> 的统一代码规范</li>
            <li>基于 <strong>axios</strong> 的 RESTful API 分层封装</li>
            <li>路由懒加载 + 构建时手动分块（vendor chunking）</li>
          </ul>
        </el-descriptions-item>
      </el-descriptions>

      <el-divider />

      <el-descriptions title="原项目 vs 现代化改造对比" :column="1" border>
        <el-descriptions-item label="原技术栈">
          Vue 2 + Vue CLI + Vue Router 3 + ECharts 4 + Vetur
        </el-descriptions-item>
        <el-descriptions-item label="主要升级点">
          Vue 2 → Vue 3（Proxy 响应式）｜ Vue CLI → Vite（ESM 按需编译）｜
          Vetur → Vue-Official（Volar）｜ ECharts 4 → ECharts 5（更小的包体积）｜
          新增 Pinia + TypeScript + Element Plus + ESLint 9
        </el-descriptions-item>
      </el-descriptions>

      <el-divider />

      <div class="about-footer">
        <el-button type="primary" @click="$router.push('/')">返回首页</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { InfoFilled } from '@element-plus/icons-vue'
</script>

<style scoped lang="scss">
.about-view {
  max-width: 960px;
  margin: 0 auto;
}

.about-card {
  border-radius: 12px;
}

.about-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 16px;
  font-weight: 600;
}

.feature-list {
  margin: 0;
  padding-left: 20px;
  line-height: 2;
  color: #606266;
}

.about-footer {
  display: flex;
  justify-content: center;
  padding: 16px 0 8px;
}
</style>
