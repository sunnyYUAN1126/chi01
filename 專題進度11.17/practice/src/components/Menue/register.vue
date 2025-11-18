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
  <div class="register_container">
    <h2>註冊新帳號</h2>

    <div class="input-group">
      <p>帳號</p>
      <input type="text" v-model="username" />
    </div>

    <div class="input-group">
      <p>電子郵件</p>
      <input type="text" v-model="email" />
    </div>

    <div class="input-group">
      <p>系所</p>
      <input type="text" v-model="department" />
    </div>

    <div class="input-group">
      <p>學號</p>
      <input type="text" v-model="studentId" />
    </div>

    <div class="input-group">
      <p>密碼</p>
      <input type="password" v-model="password" />
    </div>

    <div>
      <button @click="handleRegister">註冊</button>
    </div>
  </div>
</template>

<style scoped>
*{
    padding: 0;
    margin: 0;
    list-style: none;
}
.register_container{
  margin: 100px;
}

.register_container div{
  display: flex;
  padding: 10px;
  margin: 20px;
}
.register_container p{
  width: 100px;
  background: palegoldenrod;
  text-align: center;
}
.register_container input{
  height: 20px;
}
.register_container button{
  width: 50px;
  height: 30px;
  border-radius: 20px;
}
.register_container button:hover{
  color: white;
  background: black;

}




</style>