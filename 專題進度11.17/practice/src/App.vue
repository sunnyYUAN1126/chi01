<script setup>
import { ref } from "vue"
import Login from './components/Menue/login.vue'
import Register from "./components/Menue/register.vue"
import Home from "./components/Menue/home.vue"
import Shopping_cart from "./components/Menue/shopping_cart.vue"
import Buyer_menue from "./components/Buyer/menue.vue"
import Seller_menue from "./components/Seller/menue.vue"

const currentPage = ref("home") // 預設顯示首頁
const isLoggedIn = ref(false)   // 是否登入的狀態（false=未登入） 

// 三個切換方法
function showHomePage() {
  currentPage.value = "home";
  isLoggedIn.value = true;
}
function showLoginPage() {
  currentPage.value = "login";
}
function showRegisterPage() {
  currentPage.value = "register";
}

// 登入成功
function handleLoginSuccess() {
  currentPage.value = "home";
  isLoggedIn.value = true;
}
// 登出
function logout() {
  isLoggedIn.value = false;  
  currentPage.value = "home";
}

//購物車
function showShoppingCartPage() {
  currentPage.value = "shopping_cart";
}


//會員專區
function showMemberAreaPage(){
  currentPage.value = "Member_Area";
}

function handleSwitchPage(page) {
  currentPage.value = page
}
</script>

<template>
  <div class="App_container  ">
    <nav class="menu  navbar bg-body-tertiary navbar bg-body-tertiary  navbar-expand-lg bg-body-tertiary fixed-top">

      <div class="logo" @click="showHomePage">
        二手書系統
      </div>
      <ul>
        <li @click="showShoppingCartPage">
          購物車
          <i class="bi bi-cart4"></i>
        </li>
        <!-- 如果已登入，顯示登出 -->
        <template v-if="isLoggedIn" class="menu_item">
          <li @click="logout">登出</li>
          <li @click="showMemberAreaPage">會員專區</li>
        </template>

        <!-- 如果沒登入，顯示登入、註冊 -->
        <template v-else class="menu_item">
          <li @click="showLoginPage">登入</li>
          <li @click="showRegisterPage">註冊</li>
        </template>
      </ul>
    </nav>
  </div>


  




  <!-- 根據 currentPage 顯示不同畫面 -->
  <Home v-if="currentPage === 'home'" />  
  <Shopping_cart v-if="currentPage === 'shopping_cart'" />
  <Buyer_menue 
    v-if="currentPage === 'Member_Area'" 
    @switchPage="handleSwitchPage"
  />  
  <Seller_menue 
    v-if="currentPage === 'seller'" 
    @switchPage="handleSwitchPage"
  />
  <Login 
    v-else-if="currentPage === 'login'" 
    @login-success="handleLoginSuccess" 
    @login-Register="currentPage = 'register'"
  />
  <Register 
    v-else-if="currentPage === 'register'"
    @register-success="currentPage = 'login'"  
  />










  
</template>

<style scoped>
*{
    padding: 0;
    margin: 0;
    list-style: none;
}

.menu{
    background: rgb(216, 210, 211)  !important;
    padding: 0 50px;
}
.App_container .menu {
    background: rgb(216, 210, 211);
    display: flex;
    flex-direction: row; 
    flex-wrap: wrap; 
    justify-content: space-between; /*主軸*/
    padding: 0 20px;
    align-items: center; /*控制垂直對其*/
}
.App_container .logo{
    color: black;
    font-size: 50px;
    padding: 10px 0px;
}
.App_container .logo:hover,.App_container li:hover{
  color: aliceblue;
  font-weight: bold;
}

.App_container ul{
    display: flex; 
    gap: 10px;
}




</style>