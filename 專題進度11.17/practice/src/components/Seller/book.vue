<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h2 class="text-2xl font-bold mb-4">📘 新增書籍請求</h2>

    <!-- 新增請求 -->
    <div class="bg-gray-100 p-4 rounded-2xl shadow mb-6">
      <h3 class="text-lg font-semibold mb-3">填寫請求資料</h3>

      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block font-medium mb-1">ISBN</label>
          <input
            v-model="newRequest.isbn"
            type="text"
            placeholder="請輸入 ISBN"
            class="border rounded-lg px-3 py-2 w-full"
          />
        </div>

        <div>
          <label class="block font-medium mb-1">書籍名稱</label>
          <input
            v-model="newRequest.name"
            type="text"
            placeholder="請輸入書名"
            class="border rounded-lg px-3 py-2 w-full"
          />
        </div>
      </div>

      <button
        @click="addRequest"
        class="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        送出請求
      </button>
    </div>

    <!-- 請求紀錄 -->
    <div class="bg-white p-4 rounded-2xl shadow">
      <h3 class="text-lg font-semibold mb-3">我的書籍請求紀錄</h3>

      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-200">
            <th class="p-2 text-left">ISBN</th>
            <th class="p-2 text-left">書名</th>
            <th class="p-2 text-left">請求日期</th>
            <th class="p-2 text-left">審核狀態</th>
            <th class="p-2 text-left">管理員備註</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(req, index) in requests"
            :key="index"
            class="border-b hover:bg-gray-50"
          >
            <td class="p-2">{{ req.isbn }}</td>
            <td class="p-2">{{ req.name }}</td>
            <td class="p-2">{{ req.date }}</td>
            <td class="p-2">
              <span
                :class="{
                  'text-yellow-600': req.status === '待審核',
                  'text-green-600': req.status === '通過',
                  'text-red-600': req.status === '拒絕',
                }"
              >
                {{ req.status }}
              </span>
            </td>
            <td class="p-2">{{ req.adminNote || '-' }}</td>
          </tr>
          <tr v-if="requests.length === 0">
            <td colspan="5" class="text-center py-4 text-gray-500">
              尚無請求紀錄
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

// 新請求資料
const newRequest = ref({
  isbn: "",
  name: "",
});

// 模擬請求紀錄
const requests = ref([
  {
    isbn: "9781234567890",
    name: "Vue 3 快速入門",
    date: "2025-11-13",
    status: "通過",
    adminNote: "書籍已新增至系統",
  },
  {
    isbn: "9789876543210",
    name: "Java Web 開發實戰",
    date: "2025-11-10",
    status: "待審核",
    adminNote: "",
  },
]);

// 新增請求
function addRequest() {
  if (!newRequest.value.isbn || !newRequest.value.name) {
    alert("請輸入 ISBN 與書名");
    return;
  }

  const today = new Date().toISOString().slice(0, 10);
  requests.value.push({
    isbn: newRequest.value.isbn,
    name: newRequest.value.name,
    date: today,
    status: "待審核",
    adminNote: "",
  });

  // 清空欄位
  newRequest.value.isbn = "";
  newRequest.value.name = "";
}
</script>

<style scoped>
table th,
table td {
  border-bottom: 1px solid #e5e7eb;
}
</style>
