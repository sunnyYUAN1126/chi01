<script setup>
import { onMounted, useTemplateRef, ref } from "vue";
import { useTodoStore } from "@/stores/todo.js"

const dialog = useTemplateRef('dialog')
const todoStore = useTodoStore()
const todo = ref({})

function openModal(id) {
  todo.value = todoStore.getTodoById(id)
  dialog.value.showModal()
}

function updateTodo(id) {
  todoStore.updateTodo(id)
  dialog.value.close()
}

onMounted(todoStore.getTodos)
</script>

<template>
  <li v-for="todo in todoStore.todos" :key="todo.id">
    <div class="item-content">
      <label>
        <input :checked="todo.completed_at" @click="todoStore.toggleTodo(todo.id)" type="checkbox" />
        <p :class="todo.completed_at ? 'line-through': ''">{{ todo.content }}</p>
      </label>
    </div>
    <div class="item-control">
      <a @click.prevent="openModal(todo.id)" href="#" class="edit">edit</a>
      <a @click.prevent="todoStore.removeTodo(todo.id)" href="#" class="delete">delete</a>
    </div>
  </li>

  <dialog ref="dialog" class="modal">
    <div class="modal-box">
      <h3 class="text-lg font-bold">更新</h3>
      <p class="py-4">
        <input @keyup.enter="updateTodo(todo.id)" v-model="todo.content" type="text" class="input w-full">
      </p>
      <div class="modal-action">
        <form method="dialog" class="flex gap-2">
          <a href="#" @click="updateTodo(todo.id)" class="btn btn-success">更新</a>
          <button class="btn">取消</button>
        </form>
      </div>
    </div>
  </dialog>
</template>
