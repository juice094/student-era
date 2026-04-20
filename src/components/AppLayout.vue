<template>
  <el-container class="app-layout">
    <!-- 侧边栏 -->
    <el-aside :width="isCollapse ? '64px' : '220px'" class="sidebar">
      <div class="logo">
        <el-icon size="28" color="#fff"><DataLine /></el-icon>
        <span v-show="!isCollapse" class="logo-text">教务平台</span>
      </div>

      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapse"
        :collapse-transition="false"
        background-color="#1e293b"
        text-color="#94a3b8"
        active-text-color="#fff"
        @select="handleMenuSelect"
      >
        <el-menu-item
          v-for="menu in filteredMenus"
          :key="menu.path"
          :index="menu.path"
        >
          <el-icon><component :is="menu.icon" /></el-icon>
          <template #title>{{ menu.title }}</template>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <!-- 顶部 Header -->
      <el-header class="app-header" height="64px">
        <div class="header-left">
          <el-icon class="collapse-btn" @click="toggleCollapse">
            <Fold v-if="!isCollapse" />
            <Expand v-else />
          </el-icon>
          <Breadcrumb />
        </div>

        <div class="header-right">
          <el-dropdown @command="handleCommand">
            <span class="user-info">
              <el-avatar :size="32" :icon="UserFilled" />
              <span class="username">{{ userStore.userInfo?.realName }}</span>
              <el-icon><ArrowDown /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="role" disabled>
                  角色：{{ roleName }}
                </el-dropdown-item>
                <el-dropdown-item divided command="logout">
                  退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 内容区 -->
      <el-main class="app-main">
        <RouterView :key="route.fullPath" />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { DataLine, Fold, Expand, UserFilled, ArrowDown } from '@element-plus/icons-vue'
import { useUserStore } from '@/stores/user'
import { ROLE_NAMES } from '@/utils/permission'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const isCollapse = ref(false)

const activeMenu = computed(() => route.path)

const roleName = computed(() => {
  const role = userStore.userInfo?.role
  return role ? ROLE_NAMES[role] : ''
})

const allMenus = [
  { path: '/', title: '首页概览', icon: 'HomeFilled', code: 'Home' },
  { path: '/student', title: '学生管理', icon: 'UserFilled', code: 'Student' },
  { path: '/teacher', title: '教师管理', icon: 'UserFilled', code: 'Teacher' },
  { path: '/course', title: '课程管理', icon: 'Reading', code: 'Course' },
  { path: '/score', title: '成绩管理', icon: 'TrendCharts', code: 'Score' },
  { path: '/course-select', title: '学生选课', icon: 'Plus', code: 'CourseSelect' },
  { path: '/schedule', title: '排课管理', icon: 'Calendar', code: 'Schedule' },
  { path: '/evaluation', title: '评教结果', icon: 'Star', code: 'Evaluation' },
  { path: '/operation-log', title: '操作日志', icon: 'Document', code: 'OperationLog' },
  { path: '/about', title: '关于系统', icon: 'InfoFilled', code: 'About' }
]

const filteredMenus = computed(() =>
  allMenus.filter((m) => userStore.checkMenu(m.code))
)

function toggleCollapse() {
  isCollapse.value = !isCollapse.value
}

function handleMenuSelect(index: string) {
  if (index !== route.path) {
    router.push(index)
  }
}

function handleCommand(cmd: string) {
  if (cmd === 'logout') {
    ElMessageBox.confirm('确定退出登录吗？', '提示', { type: 'warning' }).then(() => {
      userStore.logout()
      router.push('/login')
      ElMessage.success('已退出登录')
    })
  }
}
</script>

<style scoped lang="scss">
.app-layout {
  min-height: 100vh;
}

.sidebar {
  background: #1e293b;
  transition: width 0.3s;
}

.logo {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  border-bottom: 1px solid #334155;
}

.logo-text {
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  white-space: nowrap;
}

.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  padding: 0 24px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.collapse-btn {
  font-size: 20px;
  color: #606266;
  cursor: pointer;
  &:hover {
    color: #409eff;
  }
}

.header-right {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #606266;
  .username {
    font-size: 14px;
  }
}

.app-main {
  background: #f5f7fa;
  padding: 20px;
}
</style>
