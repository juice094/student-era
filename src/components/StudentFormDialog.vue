<template>
  <el-dialog
    v-model="dialogVisible"
    :title="isEdit ? '编辑学生信息' : '新增学生'"
    width="520px"
    destroy-on-close
    :close-on-click-modal="false"
    @closed="handleClosed"
  >
    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-width="90px"
      status-icon
    >
      <el-form-item label="学号" prop="id">
        <el-input
          v-model.number="form.id"
          placeholder="请输入学号"
          :disabled="isEdit"
          clearable
        />
      </el-form-item>

      <el-form-item label="姓名" prop="name">
        <el-input v-model="form.name" placeholder="请输入姓名" clearable />
      </el-form-item>

      <el-form-item label="性别" prop="gender">
        <el-radio-group v-model="form.gender">
          <el-radio label="男">男</el-radio>
          <el-radio label="女">女</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="年龄" prop="age">
        <el-input-number v-model="form.age" :min="15" :max="50" />
      </el-form-item>

      <el-form-item label="专业" prop="major">
        <el-select v-model="form.major" placeholder="请选择专业" style="width: 100%">
          <el-option
            v-for="m in majorOptions"
            :key="m"
            :label="m"
            :value="m"
          />
        </el-select>
      </el-form-item>

      <el-form-item label="年级" prop="grade">
        <el-select v-model="form.grade" placeholder="请选择年级" style="width: 100%">
          <el-option label="大一" value="大一" />
          <el-option label="大二" value="大二" />
          <el-option label="大三" value="大三" />
          <el-option label="大四" value="大四" />
        </el-select>
      </el-form-item>

      <el-form-item label="入学年份" prop="enrollmentYear">
        <el-input-number v-model="form.enrollmentYear" :min="2015" :max="2030" />
      </el-form-item>
    </el-form>

    <template #footer>
      <el-button @click="dialogVisible = false">取消</el-button>
      <el-button type="primary" @click="handleSubmit">确定</el-button>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { ElMessage } from 'element-plus'
import type { FormInstance, FormRules } from 'element-plus'
import type { Student } from '@/types'

interface Props {
  visible: boolean
  data?: Student | null
}

const props = withDefaults(defineProps<Props>(), {
  data: null
})

const emit = defineEmits<{
  'update:visible': [value: boolean]
  submit: [data: Student]
}>()

const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

const isEdit = computed(() => !!props.data)

const formRef = ref<FormInstance>()

const defaultForm: Student = {
  id: 0,
  name: '',
  gender: '男',
  age: 18,
  major: '',
  grade: '大一',
  enrollmentYear: new Date().getFullYear()
}

const form = ref<Student>({ ...defaultForm })

const majorOptions = [
  '计算机科学与技术',
  '软件工程',
  '电子信息工程',
  '经济管理',
  '机械工程',
  '土木工程',
  '艺术设计',
  '外语'
]

const rules: FormRules = {
  id: [
    { required: true, message: '请输入学号', trigger: 'blur' },
    { type: 'number', message: '学号必须为数字', trigger: 'blur' }
  ],
  name: [
    { required: true, message: '请输入姓名', trigger: 'blur' },
    { min: 2, max: 10, message: '姓名长度2-10位', trigger: 'blur' }
  ],
  gender: [{ required: true, message: '请选择性别', trigger: 'change' }],
  age: [{ required: true, message: '请输入年龄', trigger: 'blur' }],
  major: [{ required: true, message: '请选择专业', trigger: 'change' }],
  grade: [{ required: true, message: '请选择年级', trigger: 'change' }],
  enrollmentYear: [{ required: true, message: '请输入入学年份', trigger: 'blur' }]
}

watch(
  () => props.visible,
  (val) => {
    if (val) {
      form.value = props.data ? { ...props.data } : { ...defaultForm }
    }
  },
  { immediate: true }
)

function handleClosed() {
  formRef.value?.resetFields()
}

async function handleSubmit() {
  if (!formRef.value) return
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return

  emit('submit', { ...form.value })
  ElMessage.success(isEdit.value ? '编辑成功' : '新增成功')
  dialogVisible.value = false
}
</script>
