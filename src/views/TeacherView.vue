<template>
  <div class="teacher-view">
    <el-card shadow="never">
      <template #header>
        <div class="card-header">
          <span>教师信息列表</span>
          <el-button v-permission="'teacher:add'" type="primary" @click="handleAdd">新增教师</el-button>
        </div>
      </template>

      <el-table :data="teacherStore.teachers" stripe border>
        <el-table-column prop="teacherNo" label="工号" width="120" />
        <el-table-column prop="name" label="姓名" width="100" />
        <el-table-column prop="gender" label="性别" width="80" />
        <el-table-column prop="age" label="年龄" width="80" />
        <el-table-column prop="title" label="职称" width="100" />
        <el-table-column prop="collegeName" label="所属学院" />
        <el-table-column prop="courses" label="授课课程">
          <template #default="{ row }">
            <el-tag v-for="c in row.courses" :key="c" size="small" style="margin-right: 4px">{{ c }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button v-permission="'teacher:edit'" link type="primary" size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button v-permission="'teacher:delete'" link type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑教师' : '新增教师'" width="520px" destroy-on-close>
      <el-form :model="form" label-width="90px">
        <el-form-item label="工号"><el-input v-model="form.teacherNo" :disabled="isEdit" /></el-form-item>
        <el-form-item label="姓名"><el-input v-model="form.name" /></el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="form.gender"><el-radio label="男">男</el-radio><el-radio label="女">女</el-radio></el-radio-group>
        </el-form-item>
        <el-form-item label="年龄"><el-input-number v-model="form.age" :min="22" :max="70" /></el-form-item>
        <el-form-item label="职称">
          <el-select v-model="form.title" style="width: 100%"><el-option label="教授" value="教授" /><el-option label="副教授" value="副教授" /><el-option label="讲师" value="讲师" /><el-option label="助教" value="助教" /></el-select>
        </el-form-item>
        <el-form-item label="所属学院">
          <el-select v-model="form.collegeId" style="width: 100%">
            <el-option v-for="c in dictStore.getDict('college')" :key="c.value" :label="c.label" :value="c.value" />
          </el-select>
        </el-form-item>
        <el-form-item label="电话"><el-input v-model="form.phone" /></el-form-item>
        <el-form-item label="邮箱"><el-input v-model="form.email" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useTeacherStore } from '@/stores/teacher'
import { useDictStore } from '@/stores/dict'
import type { Teacher } from '@/types/teacher'

const teacherStore = useTeacherStore()
const dictStore = useDictStore()
const dialogVisible = ref(false)
const isEdit = ref(false)

const defaultForm: Teacher = {
  id: 0, teacherNo: '', name: '', gender: '男', age: 30, title: '讲师',
  collegeId: 1, collegeName: '', phone: '', email: ''
}
const form = ref<Teacher>({ ...defaultForm })

onMounted(() => teacherStore.loadTeachers())

function handleAdd() {
  isEdit.value = false
  form.value = { ...defaultForm, id: Date.now() }
  dialogVisible.value = true
}

function handleEdit(row: Teacher) {
  isEdit.value = true
  form.value = { ...row }
  dialogVisible.value = true
}

function handleSubmit() {
  const college = dictStore.getDict('college').find((c) => c.value === form.value.collegeId)
  form.value.collegeName = college?.label ?? ''

  if (isEdit.value) teacherStore.updateTeacher(form.value)
  else teacherStore.addTeacher(form.value)

  ElMessage.success(isEdit.value ? '编辑成功' : '新增成功')
  dialogVisible.value = false
}

function handleDelete(row: Teacher) {
  ElMessageBox.confirm(`确定删除教师 "${row.name}" 吗？`, '提示', { type: 'warning' }).then(() => {
    teacherStore.deleteTeacher(row.id)
    ElMessage.success('删除成功')
  })
}
</script>

<style scoped lang="scss">
.teacher-view {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
  font-size: 15px;
}
</style>
