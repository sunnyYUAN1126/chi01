<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h2 class="text-2xl font-bold mb-6 text-center">我的訂單</h2>
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead class="bg-gray-200">
          <tr>
            <th class="py-2 px-4 text-left">訂單編號</th>
            <th class="py-2 px-4 text-left">賣家用戶</th>
            <th class="py-2 px-4 text-left">書籍名稱</th>
            <th class="py-2 px-4 text-left">isbn</th>
            <th class="py-2 px-4 text-left">訂單金額</th>
            <th class="py-2 px-4 text-left">面交地點</th>
            <th class="py-2 px-4 text-left">面交日期</th>
            <th class="py-2 px-4 text-left">面交時間</th>
            <th class="py-2 px-4 text-left">訂單狀態</th>
            <th class="py-2 px-4 text-left">下單日期</th>
            <th class="py-2 px-4 text-left">取消訂單</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orders" :key="order.id" class="border-b hover:bg-gray-50">
            <td class="py-2 px-4">{{ order.orderNo }}</td>
            <td class="py-2 px-4">{{ order.sellerName }}</td>
            <td class="py-2 px-4">{{ order.bookName }}</td>
            <td class="py-2 px-4">{{ order.isbn }}</td>
            <td class="py-2 px-4">{{ order.amount }}</td>
            <td class="py-2 px-4">{{ order.location }}</td>
            <td class="py-2 px-4">{{ order.date }}</td>
            <td class="py-2 px-4">{{ order.time }}</td>
            <td class="py-2 px-4">
              <span 
                :class="{
                  'text-yellow-600': order.status === '代面交',
                  'text-green-600': order.status === '交易完成',
                  'text-red-600': order.status === '取消'
                }"
                class="font-semibold"
              >
                {{ order.status }}
              </span>
            </td>
            <td class="py-2 px-4">{{ order.orderDate }}</td>
            <td class="py-2 px-4">
              <!-- 只有代面交才顯示 -->
              <button 
                v-if="order.status === '代面交'"   
                @click="cancelOrder(order)" 
                class="bg-white text-black border border-black px-3 py-1 rounded hover:bg-gray-200"
              >
                取消訂單
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

const orders = reactive([
  { id: 1, orderNo: 'No.1', sellerName: 'seam', bookName: '資料庫系統概論', isbn: '9789865023456', amount: 350, location: '台北車站', date: '2025/11/10', time: '上午10:00', status: '代面交', orderDate: '2025/10/25' },
  { id: 2, orderNo: 'No.2', sellerName: 'luna', bookName: 'Java 程式設計', isbn: '9789864349281', amount: 420, location: '中山捷運站', date: '2025/11/12', time: '下午2:00', status: '代面交', orderDate: '2025/10/28' },
  { id: 3, orderNo: 'No.3', sellerName: 'sunny', bookName: 'Python 入門指南', isbn: '9789863471120', amount: 280, location: '板橋車站', date: '2025/11/15', time: '下午4:00', status: '交易完成', orderDate: '2025/10/30' },
]);

function cancelOrder(order) {
  if (confirm(`確定要取消訂單 ${order.orderNo} 嗎？`)) {
    order.status = '取消';
    // 可在這裡呼叫 API 更新後端
    // axios.post('/api/orders/cancel', { orderId: order.id })
    //   .then(() => console.log('取消成功'))
    //   .catch(err => console.error(err))
  }
}
</script>
