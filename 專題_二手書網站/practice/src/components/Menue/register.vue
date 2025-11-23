<script setup>
import { ref } from "vue"

// 宣告可以往父層發出事件
const emit = defineEmits(["register-success"])

const username = ref("")
const email = ref("")
const department = ref("")
const studentId = ref("")
const password = ref("")

function handleRegister() {
  // 這裡可以先做一些基本檢查
  if (!username.value || !email.value || !department.value || !studentId.value || !password.value) {
    alert("請填寫完整註冊資料！")
    return
  }

  // 假裝成功註冊  alert() 是 JavaScript 內建的「彈出通知視窗」
  alert("註冊成功！請登入。")

  // 通知父層回到登入畫面
  emit("register-success")
}
</script>

<template>

<div class="login_container card mx-auto text-center" style="width: 40%;">
  <!-- 標題區 -->
  <div class="startlogin p-4" style="background-color: gray; color: white; border-radius: 5px 5px 0 0;">
    <h2 class="mb-0">註冊新帳號</h2>
  </div>

  <!-- 帳號 -->
  <div class="input-group mb-4 mt-4 mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 30%;">帳號</span>
    <input type="text" class="form-control text-center" v-model="username" placeholder="Username">
  </div>

  <!-- 電子郵件 -->
  <div class="input-group mb-4  mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 30%;">電子郵件</span>
    <input type="text" class="form-control text-center" v-model="email" placeholder="Email">
  </div>

  <!-- 系所 -->
  <div class="input-group mb-4  mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 30%;">系所</span>
    <input type="text" class="form-control text-center" v-model="department" placeholder="Department">
  </div>

  <!-- 學號 -->
  <div class="input-group mb-4  mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 30%;">學號</span>
    <input type="text" class="form-control text-center" v-model="studentId" placeholder="studentId">
  </div>

  <!-- 密碼 -->
  <div class="input-group mb-4  mx-auto" style="width: 70%;">
    <span class="input-group-text d-flex justify-content-center align-items-center" style="width: 30%;">密碼</span>
    <input type="password" class="form-control text-center" v-model="password" placeholder="Password">
  </div>


  <!-- 註冊 -->
  <div class="mb-4 mt-4 d-flex justify-content-center align-items-center gap-2">
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