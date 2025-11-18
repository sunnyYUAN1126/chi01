<template>
  <div class="p-4">
    <!-- 選單切換 -->
    <div class="mb-4">
      <button @click="currentTab = 'current'" :class="{'font-bold': currentTab === 'current'}">目前訂單</button>
      <button @click="currentTab = 'history'" :class="{'font-bold': currentTab === 'history'}">歷史訂單</button>
    </div>

    <!-- 目前訂單表格 -->
    <table v-if="currentTab === 'current'" border="1" cellpadding="5">
      <thead>
        <tr>
          <th>項目</th>
          <th>訂單編號</th>
          <th>賣家名稱</th>
          <th>商品數量</th>
          <th>訂單金額</th>
          <th>面交日期</th>
          <th>面交時間</th>
          <th>訂單狀態</th>
          <th>下單日期</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(order, index) in currentOrders" :key="order.id">
          <td>{{ index + 1 }}</td>
          <td>{{ order.orderNo }}</td>
          <td>{{ order.seller }}</td>
          <td>{{ order.productCount }}</td>
          <td>{{ order.amount }}</td>
          <td>{{ order.date }}</td>
          <td>{{ order.time }}</td>
          <td>{{ order.status }}</td> <!-- 這裡變成純文字 -->
          <td>{{ order.orderDate }}</td>
          <td>
            <button @click="viewDetail(order)">明細</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 歷史訂單表格 -->
    <table v-if="currentTab === 'history'" border="1" cellpadding="5">
      <thead>
        <tr>
          <th>項目</th>
          <th>訂單編號</th>
          <th>賣家名稱</th>
          <th>商品數量</th>
          <th>訂單金額</th>
          <th>面交日期</th>
          <th>面交時間</th>
          <th>訂單狀態</th>
          <th>下單日期</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(order, index) in historyOrders" :key="order.id">
          <td>{{ index + 1 }}</td>
          <td>{{ order.orderNo }}</td>
          <td>{{ order.seller }}</td>
          <td>{{ order.productCount }}</td>
          <td>{{ order.amount }}</td>
          <td>{{ order.date }}</td>
          <td>{{ order.time }}</td>
          <td>{{ order.status }}</td>
          <td>{{ order.orderDate }}</td>
          <td>
            <button @click="viewDetail(order)">明細</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 明細彈窗 -->
    <div v-if="selectedOrder" class="fixed top-0 left-0 w-full h-full bg-black/50 flex justify-center items-center">
      <div class="bg-white p-6 rounded-lg w-1/2">
        <h3 class="text-lg font-bold mb-4">訂單 {{ selectedOrder.orderNo }} 明細</h3>
        <table border="1" cellpadding="5" class="w-full mb-4">
          <thead>
            <tr>
              <th>商品名稱</th>
              <th>價錢</th>
              <th>數量</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in selectedOrder.items" :key="item.name">
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.quantity }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2">總計</td>
              <td>{{ selectedOrder.items.reduce((sum, i) => sum + i.price * i.quantity, 0) }}</td>
            </tr>
          </tfoot>
        </table>
        <button @click="selectedOrder = null">關閉</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

// 模擬買家的目前訂單
const currentOrders = reactive([
  { 
    id: 1, 
    orderNo: 'A001', 
    seller: '貓書店', 
    productCount: 2, 
    amount: 300, 
    date: '2025/11/1', 
    time: '上午11:00', 
    status: '待面交', 
    orderDate: '2025/10/28',
    items: [
      { name: '貓咪的旅程', price: 200, quantity: 1 },
      { name: '狗狗的秘密', price: 100, quantity: 1 },
    ]
  },
])

// 模擬歷史訂單
const historyOrders = reactive([
  { 
    id: 2, 
    orderNo: 'A005', 
    seller: '陽光書屋', 
    productCount: 3, 
    amount: 600, 
    date: '2025/10/10', 
    time: '下午5:00', 
    status: '完成', 
    orderDate: '2025/10/5',
    items: [
      { name: '書A', price: 100, quantity: 1 },
      { name: '書B', price: 150, quantity: 2 },
    ]
  },
])

const currentTab = ref('current')
const selectedOrder = ref(null)

function viewDetail(order) {
  selectedOrder.value = order
}
</script>
