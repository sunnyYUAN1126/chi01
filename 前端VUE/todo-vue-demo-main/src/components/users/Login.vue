<script setup>
import { ref } from 'vue';
import { appAlert } from '@/lib/utils';
import { createAxios } from "@/lib/http.js"

const emits = defineEmits(['sign_up', 'task_input'])

const email = ref("")
const password = ref("")

async function login() {
  const userData = {
    user: {
      email: email.value,
      password: password.value
    }
  }

  try {
    const ax = createAxios()
    const result = await ax.post('/users/sign_in', userData)

    const token = result.headers.authorization

    if (token) {
      localStorage.setItem("token", token)
    }

    emits('task_input')
  } catch (err) {
    const { error, message } = err.response.data;
    const errorMessage = `${message}: ${error.join(' / ')}`

    appAlert(errorMessage)
  }
}
</script>

<template>
  <section id="loginSection">
    <h1>登入</h1>
    <form id="loginForm">
      <div class="field">
        <label>
          <h3>Email</h3>
          <input type="email" v-model="email" autocomplete="off" spellcheck="false" placeholder="Email 信箱" />
        </label>
      </div>

      <div class="field">
        <label>
          <h3>密碼</h3>
          <input type="password" v-model="password" autocomplete="off" spellcheck="false" placeholder="密碼，至少需要 6 個字" />
        </label>
      </div>

      <div class="items-center justify-between block sm:flex field">
        <button @click.prevent="login">登入</button>
        <div class="text-xl text-gray-600">還沒有帳號嗎？
          <a @click.prevent="$emit('sign_up')" href="#" class="text-link signUpLink">註冊</a>一個吧！</div>
      </div>
    </form>
  </section>
</template>
