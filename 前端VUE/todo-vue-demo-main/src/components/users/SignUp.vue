<script setup>
import { appAlert } from '@/lib/utils';
import { ref } from 'vue';
import { createAxios } from "@/lib/http.js"

const emits = defineEmits(['login'])

const email = ref("")
const nickname = ref("")
const password = ref("")

async function register() {
  const userData = {
    user: {
      email: email.value,
      nickname: nickname.value,
      password: password.value
    }
  }

  try {
    const ax = createAxios()
    await ax.post('/users', userData)
    emits('login')
  } catch (err) {
    const { error, message } = err.response.data;
    const errorMessage = `${message}: ${error.join(' / ')}`

    appAlert(errorMessage)
  }
}
</script>

<template>
  <section id="signUpSection">
    <h1>註冊帳號</h1>
    <form id="signUpForm">
      <div class="field">
        <label>
          <h3>Email</h3>
          <input v-model="email" type="email" autocomplete="off" spellcheck="false" placeholder="Email 信箱" />
        </label>
      </div>

      <div class="field">
        <label>
          <h3>暱稱</h3>
          <input v-model="nickname" type="text" autocomplete="off" spellcheck="false" placeholder="要怎麼稱呼你呢？" />
        </label>
      </div>

      <div class="field">
        <label>
          <h3>密碼</h3>
          <input v-model="password" type="password" autocomplete="off" spellcheck="false" placeholder="密碼，至少需要 6 個字" />
        </label>
      </div>

      <div class="items-center justify-between block sm:flex field">
        <button @click.prevent="register">註冊</button>
        <div class="text-xl text-gray-600">已經有帳號了？<a @click.prevent="$emit('login')" href="#" class="text-link loginLink">登入</a></div>
      </div>
    </form>
  </section>
</template>
