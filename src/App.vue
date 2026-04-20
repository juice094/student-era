<template>
  <div class="app-wrapper">
    <AppHeader />
    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
</script>

<style scoped lang="scss">
.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
}
.app-main {
  flex: 1;
  padding: 24px;
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
}
</style>
