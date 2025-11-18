<script setup>
import history from './history.vue'
import order from './order.vue'
import product from './product.vue'
import book from './book.vue'

// 目前顯示哪個頁面
import { ref } from 'vue'
const currentPage = ref('order') // 預設顯示訂單交易

// 切換頁面
function switchPage(page) {
  currentPage.value = page
}

// 切換回買家專區
const emit = defineEmits(['switchPage'])
function showBuyerPage() {
  emit('switchPage', 'Member_Area')
}
</script>

<template>
  <div class="seller_container">
    <nav class="menu2">
      <ul>
        <h3>賣家專區</h3>
        <li class="menu_item" @click="switchPage('product')">商品管理</li>
        <li class="menu_item" @click="switchPage('order')">訂單管理</li>
        <li class="menu_item" @click="switchPage('history')">交易歷史</li>
        <li class="menu_item" @click="switchPage('book')">新增書籍</li>
        <li class="menu_item" @click="showBuyerPage">買家專區</li>
      </ul>
    </nav>

    <!-- 主內容區 -->
    <div class="content">
      <product v-show="currentPage === 'product'" />
      <order v-show="currentPage === 'order'" />
      <history v-show="currentPage === 'history'" />
      <book v-show="currentPage === 'book'" />
    </div>
  </div>
</template>

<style scoped>
*{
    padding: 0;
    margin: 0;
    list-style: none;
}

.seller_container{
  display: flex;
}


.seller_container .menu2{
  background: rgb(176, 230, 143);
  padding: 2px;
  width: 100px;
  text-align: center;
}
.seller_container .menu2>ul>.menu_item{
  border: 1px solid plum;
}
.seller_container .menu2>ul>.menu_item:hover {
  background-color: pink; /* 滑鼠移過來會變色 */
}
.seller_container .menu_item{
    /* width: 200px; */
    color: black;
    line-height: 60px;
    font-size: 20px;
}
</style>