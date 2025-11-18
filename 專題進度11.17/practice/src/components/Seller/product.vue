<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <!-- 標題 -->
    <h1 class="text-2xl font-bold text-gray-700 mb-6">📚 商品管理</h1>

    <!-- 查詢書籍區塊（改成 ISBN 查詢） -->
    <div class="bg-white p-4 rounded-2xl shadow-md mb-6">
      <h2 class="font-semibold text-lg mb-3">🔍 以 ISBN 查詢可上架書籍</h2>
      <div class="flex space-x-3">
        <input
          v-model="searchISBN"
          type="text"
          placeholder="輸入 ISBN"
          class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-blue-400"
        />
        <button
          @click="searchBook"
          class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
        >
          查詢
        </button>
      </div>

      <!-- 搜尋結果 -->
      <div v-if="searchResults.length" class="mt-4 border-t pt-3">
        <h3 class="text-sm text-gray-500 mb-2">搜尋結果：</h3>
        <table class="w-full text-sm text-left text-gray-600">
          <thead class="bg-gray-100 text-gray-700 uppercase text-xs">
            <tr>
              <th class="px-4 py-2">ISBN</th>
              <th class="px-4 py-2">書名</th>
              <th class="px-4 py-2 text-center">操作</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(book, index) in searchResults"
              :key="index"
              class="border-b hover:bg-gray-50"
            >
              <td class="px-4 py-2">{{ book.isbn }}</td>
              <td class="px-4 py-2">{{ book.name }}</td>
              <td class="px-4 py-2 text-center">
                <button
                  @click="selectBook(book)"
                  class="bg-green-600 text-white px-3 py-1 rounded-lg hover:bg-green-700 text-xs"
                >
                  選擇
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <p v-if="searchResults.length === 0 && searchDone" class="text-gray-500 mt-3 text-sm">
        ❌ 查無此 ISBN 的書籍
      </p>
    </div>

    <!-- 商品清單 -->
    <div class="flex justify-between items-center mb-3">
      <h2 class="font-semibold text-lg text-gray-700">🗂️ 已上架商品</h2>
    </div>

    <div class="bg-white shadow-md rounded-2xl overflow-hidden">
      <table class="w-full text-sm text-left text-gray-600">
        <thead class="bg-gray-100 text-gray-700 uppercase text-xs">
          <tr>
            <th class="px-6 py-3">isbn</th>
            <th class="px-6 py-3">書名</th>
            <th class="px-6 py-3">商品狀況</th>
            <th class="px-6 py-3">是否有筆記</th>
            <th class="px-6 py-3">備註</th>
            <th class="px-6 py-3 text-right">價格</th>
            <th class="px-6 py-3 text-center">操作</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(item, index) in products"
            :key="index"
            class="border-b hover:bg-gray-50 transition"
          >
            <td class="px-6 py-4 font-medium text-gray-900">{{ item.isbn }}</td>
            <td class="px-6 py-4 font-medium text-gray-900">{{ item.name }}</td>
            <td class="px-6 py-4">{{ item.condition }}</td>
            <td class="px-6 py-4">
              <span
                :class="item.notes ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'"
                class="px-2 py-1 rounded-full text-xs font-medium"
              >
                {{ item.notes ? '有' : '無' }}
              </span>
            </td>
            <td class="px-6 py-4">{{ item.remark || '-' }}</td>
            <td class="px-6 py-4 text-right font-semibold text-blue-600">
              ${{ item.price.toLocaleString() }}
            </td>
            <td class="px-6 py-4 text-center space-x-2">
              <button
                @click="openEditModal(item, index)"
                class="text-yellow-600 hover:text-yellow-800 font-medium"
              >
                編輯
              </button>
              <button
                @click="deleteProduct(index)"
                class="text-red-600 hover:text-red-800 font-medium"
              >
                刪除
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 新增 / 編輯商品 Modal -->
    <div
      v-if="showModal"
      class="fixed inset-0 bg-black/40 flex items-center justify-center z-50"
    >
      <div class="bg-white p-6 rounded-2xl shadow-lg w-[400px]">
        <h2 class="text-xl font-semibold mb-4">
          {{ editingIndex !== null ? '編輯商品' : '新增商品' }}
        </h2>

        <div class="space-y-3">
          <input v-model="form.isbn" type="text" disabled class="input bg-gray-100" />
          <input v-model="form.name" type="text" disabled class="input bg-gray-100" />
          <input v-model="form.condition" type="text" placeholder="商品狀況 (幾成新)" class="input" />
          <select v-model="form.notes" class="input">
            <option :value="true">有筆記</option>
            <option :value="false">無筆記</option>
          </select>
          <input v-model="form.remark" type="text" placeholder="備註" class="input" />
          <input v-model.number="form.price" type="number" placeholder="價格" class="input" />
        </div>

        <div class="mt-6 flex justify-end space-x-3">
          <button @click="closeModal" class="px-4 py-2 bg-gray-300 rounded-lg hover:bg-gray-400">
            取消
          </button>
          <button
            @click="saveProduct"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            儲存
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 已上架商品
const products = ref([
  {
    isbn: '9789571234567',
    name: '資料結構入門',
    condition: '九成新',
    notes: true,
    remark: '封面微摺',
    price: 350
  }
])

// 模擬管理員已審核書籍清單（加上 ISBN）
const approvedBooks = [
  { isbn: '9789571234567', name: '資料結構入門' },
  { isbn: '9789577654321', name: 'Python 程式設計' },
  { isbn: '9789861122334', name: '行銷學概論' },
  { isbn: '9789579876543', name: '資料庫系統原理' },
  { isbn: '123', name: '貓' }
]

// 搜尋用（改成 ISBN）
const searchISBN = ref('')
const searchResults = ref([])
const searchDone = ref(false)

function searchBook() {
  const isbn = searchISBN.value.trim()
  searchDone.value = true
  if (!isbn) {
    searchResults.value = []
    return
  }
  // 用 ISBN 完全比對
  const result = approvedBooks.filter(b => b.isbn === isbn)
  searchResults.value = result
}

function selectBook(book) {
  resetForm()
  form.value.isbn = book.isbn
  form.value.name = book.name 
  editingIndex.value = null
  showModal.value = true
}

// Modal
const showModal = ref(false)
const editingIndex = ref(null)
const form = ref({
  isbn:'',
  name: '',
  condition: '',
  notes: false,
  remark: '',
  price: null
})

function openEditModal(item, index) {
  editingIndex.value = index
  form.value = { ...item }
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

function resetForm() {
  form.value = {
    isbn:'',
    name:'',
    condition: '',
    notes: false,
    remark: '',
    price: null
  }
}

function saveProduct() {
  if (!form.value.isbn) {
    alert('請先選擇一本書再新增！')
    return
  }

  if (editingIndex.value === null) {
    products.value.push({ ...form.value })
  } else {
    products.value[editingIndex.value] = { ...form.value }
  }
  closeModal()
}

function deleteProduct(index) {
  if (confirm('確定要刪除此商品嗎？')) {
    products.value.splice(index, 1)
  }
}
</script>

<style scoped>
.input {
  @apply w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400;
}
</style>
