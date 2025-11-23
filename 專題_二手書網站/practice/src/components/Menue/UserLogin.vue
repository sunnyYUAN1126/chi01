<script setup>
import { ref } from "vue"

// emit 是 Vue 3 用來發出事件的方法
const emit = defineEmits(["login-success"])

const username = ref("")
const password = ref("")

function handleLogin() {
  // 簡單模擬登入檢查
  if (username.value && password.value) {
    emit("login-success") // 通知父層登入成功
  } else {
    alert("請輸入帳號和密碼！")
  }
}

function handleRegister() {
    emit("login-Register") // 通知父層登入成功

}
</script>

<template>



<div class="login_container card mx-auto text-center" style="width: 40%;">
  <!-- 標題區 -->
  <div class="startlogin p-4" style="background-color: gray; color: white; border-radius: 5px 5px 0 0;">
    <h2 class="mb-0">會員登入</h2>
  </div>

  <!-- 帳號 -->
  <div class="input-group mb-4 mt-4 mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 20%;">帳號</span>
    <input type="text" class="form-control text-center" v-model="username" placeholder="Username">
  </div>

  <!-- 密碼 -->
  <div class="input-group mb-4  mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 20%;">密碼</span>
    <input type="password" class="form-control text-center" v-model="password" placeholder="Password">
  </div>

  <!-- 登入按鈕 -->
  <div class="mb-4 mt-4">
    <button class="btn btn-primary" @click="handleLogin">登入</button>
  </div>

  <!-- 註冊 -->
  <div class="mb-4 mt-4 d-flex justify-content-center align-items-center gap-2">
    <p class="mb-0">沒有帳號？</p>
    <button class="btn btn-secondary" @click="handleRegister">註冊</button>
  </div>
</div>

 

  

  


</template>

<style scoped>
*{
    padding: 0;
    margin: 0;
    list-style: none;
}
.login_container{
  margin: 200px;
}


.login_container button{
  width: 50px;
  height: 30px;
  border-radius: 20px;
}
.login_container button:hover{
  color: white;
  background: black;

}


</style>