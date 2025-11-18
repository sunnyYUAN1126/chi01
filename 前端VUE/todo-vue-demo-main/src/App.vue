<script setup>
import { ref, onMounted  } from "vue"
import { CONST as C } from "./lib/constants"
import axios from "axios"
import Login from "./components/users/Login.vue"
import SignUp from "./components/users/SignUp.vue"
import TaskInput from "./components/todos/TaskInput.vue"
import TodoItem from "./components/todos/TodoItem.vue"

const status = ref(C.STATUS_LOGIN)

onMounted(() => {
  const token = localStorage.getItem('token')

  if (token) {
    status.value = C.STATUS_TASKINPUT
  } else {
    status.value = C.STATUS_LOGIN
  }
})

async function logout() {
  const url = 'https://todoo.5xcamp.us/users/sign_out'
  const token = localStorage.getItem('token')

  if (token) {
    const headers = {
      Authorization: token
    }

    try {
      await axios.delete(url, {headers})
      localStorage.removeItem('token')
      gotoLogin()
    } catch (err) {
      console.log(err);
    }
  }
}

const gotoLogin = () => status.value = C.STATUS_LOGIN
const gotoSignUp = () => status.value = C.STATUS_SIGNUP
const gotoTaskInput = () => status.value = C.STATUS_TASKINPUT
</script>

<template>
  <header class="banner">
    <h1><a href="#todo" class="taskLink">TODO!</a></h1>
    <div class="subtitle">
      <p class="text">Simple and Studid TODO App</p>
      <p class="hidden text sm:block">
        powered by
        <a href="https://5xcampus.com" class="text-link" target="_blank">5xCampus</a>
        |
        <a href="https://todoo.5xcamp.us" class="text-link" target="_blank">API</a>
        |
        <a href="https://github.com/5xTraining/todoo-app" class="text-link" target="_blank">GitHub</a>
      </p>
    </div>
  </header>

  <main class="px-6 todo-app main">
    <header>
      <nav v-if="status == C.STATUS_TASKINPUT" class="navbar">
        <a @click.prevent="logout" href="#login">登出</a>
      </nav>
      <nav v-else class="navbar">
        <a @click.prevent="gotoLogin" href="#login">登入</a>
        <a @click.prevent="gotoSignUp" href="#sign_up">註冊</a>
      </nav>
    </header>

    <section id="userSection">
      <Login @task_input="gotoTaskInput" @sign_up="gotoSignUp" v-if="status == C.STATUS_LOGIN" />
      <SignUp @login="gotoLogin" v-if="status == C.STATUS_SIGNUP" />
    </section>

    <TaskInput v-if="status == C.STATUS_TASKINPUT" />
  </main>

  <section v-if="status == C.STATUS_TASKINPUT" class="todo-list">
    <ul class="items">
      <TodoItem />
    </ul>
  </section>

  <footer>
    <p>
      powered by
      <a href="https://5xcampus.com" class="underline">5XCAMPUS</a> | <a href="https://todoo.5xcamp.us" class="underline">API</a> |
      <a href="https://github.com/5xTraining/todoo-app" class="underline">SOURCE</a>
    </p>
  </footer>
</template>
