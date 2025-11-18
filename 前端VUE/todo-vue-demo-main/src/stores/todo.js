import { defineStore } from "pinia"
import { ref } from "vue"
import { createAxios } from "@/lib/http.js"

const useTodoStore = defineStore("todo", () => {
  const todos = ref([])
  const todo = ref({})

  async function getTodos() {
    try {
      const ax = createAxios()
      const { data } = await ax.get("/todos")
      todos.value = data.todos
    } catch (err) {
      console.log(err)
    }
  }

  async function addTodo(content) {
    todo.value = {
      id: null,
      content,
      completed_at: null,
    }

    todos.value.unshift(todo.value)

    const todoObj = {
      todo: { content },
    }

    try {
      const ax = createAxios()
      const { data } = await ax.post("/todos", todoObj)
      const { id } = data
      todo.value.id = id
    } catch (err) {
      console.log(err)
    }
  }

  function removeTodo(id) {
    const idx = todos.value.findIndex((t) => t.id == id)

    if (idx >= 0) {
      todos.value.splice(idx, 1)
    }

    const ax = createAxios()
    ax.delete(`/todos/${id}`)
  }

  function toggleTodo(id) {
    const todo = getTodoById(id)

    if (todo) {
      todo.completed_at = !todo.completed_at
    }

    const ax = createAxios()
    ax.patch(`/todos/${id}/toggle`)
  }

  function getTodoById(id) {
    return todos.value.find((t) => t.id == id)
  }

  function updateTodo(id) {
    const todo = getTodoById(id)

    const todoObj = {
      todo: {
        content: todo.content,
      },
    }

    const ax = createAxios()
    try {
      ax.put(`/todos/${id}`, todoObj)
    } catch (err) {
      console.log(err)
    }
  }

  return { addTodo, getTodos, removeTodo, updateTodo, toggleTodo, getTodoById, todos }
})

export { useTodoStore }
