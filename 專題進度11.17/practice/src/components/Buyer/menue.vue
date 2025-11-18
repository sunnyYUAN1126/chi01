<script setup>
import history from './history.vue'
import order from './order.vue'


// 宣告要發射的事件名稱
const emit = defineEmits(['switchPage'])

// 賣家專區
function showSelleraPage() {
  // 發送事件給父層，帶參數 "seller"
  emit('switchPage', 'seller')
}


// 目前顯示哪個頁面
import { ref } from 'vue'
const currentPage = ref('order') // 預設顯示訂單交易

// 切換頁面
function switchPage(page) {
  currentPage.value = page
}
</script>

<template>
  <div class="buyer_container">
    <nav class="menu2">
      <ul>
        <h3>買家專區</h3>
        <li class="menu_item" @click="switchPage('order')">訂單查詢</li>
        <li class="menu_item" @click="switchPage('history')">交易歷史</li>
        <li class="menu_item" @click="showSelleraPage">賣家專區</li>
      </ul>
    </nav> 

    <!-- 主內容區 -->
    <div class="content">
      <order v-show="currentPage === 'order'" />
      <history v-show="currentPage === 'history'" />
    </div>

  </div>
</template>

<style scoped>
*{
    padding: 0;
    margin: 0;
    list-style: none;
}

.buyer_container{
  display: flex;
}


.buyer_container .menu2{
  background: rgb(232, 240, 121);
  padding: 2px;
  width: 100px;
  text-align: center;
}
.buyer_container .menu2>ul>.menu_item{
  border: 1px solid plum;
}
.buyer_container .menu2>ul>.menu_item:hover {
  background-color: pink; /* 滑鼠移過來會變色 */
}
.buyer_container .menu_item{
    /* width: 200px; */
    color: black;
    line-height: 60px;
    font-size: 20px;
}
/* ------------------------------------------ */




</style>