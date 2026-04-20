<template>
  <div class="login-page">
    <el-card class="login-card" shadow="hover">
      <template #header>
        <div class="login-header">
          <h2>教务数据可视化平台</h2>
          <p>Academic Administration System</p>
        </div>
      </template>

      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-position="top"
        @keyup.enter="handleLogin"
      >
        <el-form-item label="用户名" prop="username">
          <el-input
            v-model="form.username"
            placeholder="请输入用户名"
            :prefix-icon="User"
            clearable
          />
        </el-form-item>

        <el-form-item label="密码" prop="password">
          <el-input
            v-model="form.password"
            type="password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
            clearable
          />
        </el-form-item>

        <el-form-item>
          <el-button
            type="primary"
            size="large"
            :loading="loading"
            style="width: 100%"
            @click="handleLogin"
          >
            登录
          </el-button>
        </el-form-item>
      </el-form>

      <div class="login-tips">
        <p>测试账号：</p>
        <el-tag size="small">admin / admin123</el-tag>
        <el-tag size="small" type="success">teacher / teacher123</el-tag>
        <el-tag size="small" type="warning">student / student123</el-tag>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { User, Lock } from '@element-plus/icons-vue'
import type { FormInstance, FormRules } from 'element-plus'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const formRef = ref<FormInstance>()
const loading = ref(false)

const form = ref({
  username: '',
  password: ''
})

const rules: FormRules = {
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

async function handleLogin() {
  if (!formRef.value) return
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  loading.value = true
  try {
    await userStore.login(form.value)
    ElMessage.success('登录成功')
    router.push('/')
  } catch (err: any) {
    ElMessage.error(err.message || '登录失败')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped lang="scss">
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e0f2fe 0%, #f0fdf4 50%, #fef9c3 100%);
}

.login-card {
  width: 420px;
  border-radius: 16px;
  padding: 12px 24px 24px;
}

.login-header {
  text-align: center;
  h2 {
    margin: 0;
    font-size: 24px;
    color: #1e293b;
    background: linear-gradient(90deg, #2563eb, #16a34a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  p {
    margin: 6px 0 0;
    font-size: 13px;
    color: #94a3b8;
  }
}

.login-tips {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px dashed #e2e8f0;
  p {
    margin: 0 0 8px;
    font-size: 12px;
    color: #94a3b8;
  }
  .el-tag {
    margin-right: 8px;
    margin-bottom: 6px;
  }
}
</style>
