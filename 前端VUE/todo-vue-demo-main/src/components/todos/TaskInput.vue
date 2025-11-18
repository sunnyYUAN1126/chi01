<script setup>
import { useTodoStore } from "@/stores/todo.js"
import { ref } from 'vue'

const todoStore = useTodoStore()

const content = ref('')

const addTodo = () => {
  todoStore.addTodo(content.value)
  content.value = ''
}
</script>

<template>
  <section id="taskSection">
    <form id="todoForm" @submit.prevent="addTodo">
      <input v-model="content" type="text" id="taskInput" autocomplete="off" spellcheck="false" placeholder="做點重要的事吧..." />
      <button id="addTodoBtn">新增</button>
    </form>
  </section>
</template>
