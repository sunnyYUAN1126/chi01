<script setup>
import { ref } from 'vue'

// 模擬商品資料
const products = ref([
  {
    id: 1,
    name: '特殊傳說Ⅲ vol.09000',
    author: '護玄',
    publisher: '蓋亞文化',
    pubDate: '2024/10/16',
    price: 299,
    isbn: '9786263841253',
    stock: 3,
    sold: 10,
    img: '/picture/1-1.jpg',
    sellers: [
      {
        name: '貓咪賣家',
        condition: '六成新',
        note: '少量筆記',
        status: '泛黃',
        date: '2025/1/1',
        price: 100,
        images: ['/picture/1-1.jpg','/picture/1-2.jpg','/picture/1-3.jpg']
      },
      {
        name: '狗狗賣家',
        condition: '五成新',
        note: '有',
        status: '無',
        date: '2025/1/1',
        price: 100,
        images: [
          'https://via.placeholder.com/100x100?text=A',
          'https://via.placeholder.com/100x100?text=B',
          'https://via.placeholder.com/100x100?text=C',
          'https://via.placeholder.com/100x100?text=D'
        ]
      }
    ]
  },
  {
    id: 2,
    name: '魔法書Ⅱ vol.05',
    author: '某作者',
    publisher: '某出版社',
    pubDate: '2023/05/01',
    price: 200,
    isbn: '9781234567890',
    stock: 5,
    sold: 20,
    img: 'https://via.placeholder.com/300x300',
    sellers: [
      {
        name: '小明',
        condition: '九成新',
        note: '無',
        status: '良好',
        date: '2025/2/1',
        price: 180,
        images: [
          'https://via.placeholder.com/100x100?text=X1',
          'https://via.placeholder.com/100x100?text=X2',
          'https://via.placeholder.com/100x100?text=X3',
          'https://via.placeholder.com/100x100?text=X4'
        ]
      },
      {
        name: '忠明',
        condition: '九成新',
        note: '無',
        status: '良好',
        date: '2025/2/1',
        price: 180,
        images: [
          'https://via.placeholder.com/100x100?text=X1',
          'https://via.placeholder.com/100x100?text=X2',
          'https://via.placeholder.com/100x100?text=X3',
          'https://via.placeholder.com/100x100?text=X4'
        ]
      },
      {
        name: '大明',
        condition: '九成新',
        note: '無',
        status: '良好',
        date: '2025/2/1',
        price: 180,
        images: [
          'https://via.placeholder.com/100x100?text=X1',
          'https://via.placeholder.com/100x100?text=X2',
          'https://via.placeholder.com/100x100?text=X3',
          'https://via.placeholder.com/100x100?text=X4'
        ]
      }
    ]
  }
])

// 控制頁面狀態
const showDetail = ref(false)
const selectedProduct = ref(null)

// 放大圖片控制
const zoomImg = ref(null)
function openZoom(img) { zoomImg.value = img }
function closeZoom() { zoomImg.value = null }

// 點商品卡切換詳細頁
function viewDetail(product) {
  selectedProduct.value = product
  showDetail.value = true
}

// 返回列表頁
function goBack() {
  selectedProduct.value = null
  showDetail.value = false
}
</script>

<template>
  <!-- 商品列表 -->
  <div v-if="!showDetail" class="apple row row-cols-1 row-cols-md-3 g-4">
    <div class="col" v-for="product in products" :key="product.id">
      <div class="card" @click="viewDetail(product)" style="cursor:pointer">
        <div style="text-align: center;">
          <img :src="product.img" alt="商品圖片" style="height: 300px; width: auto; display: inline-block;">
        </div>
        <div class="card-body">
          <h5 class="card-title">{{ product.name }}</h5>
          <p class="card-text">原定價: {{ product.price }}元</p>
          <p class="card-text">庫存: {{ product.stock }}</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 商品詳細頁 -->
  <div v-else class="apple1 card mx-auto my-3" style="width: 70%;">
    <button class="btn btn-secondary mb-3" @click="goBack">← 返回列表</button>

    <div class="d-flex">
      <!-- 圖片圖片~ -->
      <div style="text-align: center;">
        <img :src="selectedProduct.img" alt="商品圖片" style="height: 400px; width: auto; display: inline-block;">
      </div>
      <!-- <img :src="selectedProduct.img" style="width: 40%; object-fit: cover;" alt="商品圖片"> -->
      <div class="flex-grow-1">
        <div class="card-body">
          <h5 class="card-title">{{ selectedProduct.name }}</h5>
          <p class="card-text">作者: {{ selectedProduct.author }}</p>
          <p class="card-text">出版社: {{ selectedProduct.publisher }}</p>
          <p class="card-text">出版日期: {{ selectedProduct.pubDate }}</p>
          <p class="card-text">原定價: {{ selectedProduct.price }}元</p>
          <p class="card-text">ISBN: {{ selectedProduct.isbn }}</p>
          <p class="card-text">庫存: {{ selectedProduct.stock }}</p>
          <p class="card-text">銷售量: {{ selectedProduct.sold }}</p>
        </div>
      </div>
    </div>

    <!-- 商品販售狀態 -->
    <div class="pt-5">
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>賣家</th>
            <th>幾成新</th>
            <th>有無筆記</th>
            <th>書況</th>
            <th>上架時間</th>
            <th>二手價</th>
            <th>商品圖片 (4 張)</th>
            <th>購買</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(seller, index) in selectedProduct.sellers" :key="index">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ seller.name }}</td>
            <td>{{ seller.condition }}</td>
            <td>{{ seller.note }}</td>
            <td>{{ seller.status }}</td>
            <td>{{ seller.date }}</td>
            <td>{{ seller.price }}元</td>

            <!-- 每個賣家 4 張圖片，可點擊放大 -->
            <td>
              <div style="display: flex; gap: 5px;">
                <img
                  v-for="(img, i) in seller.images"
                  :key="i"
                  :src="img"
                  style="width: 60px; height: 60px; object-fit: cover; border-radius: 6px; cursor:pointer;"
                  @click="openZoom(img)"
                >
              </div>
            </td>

            <td>
              <button class="btn btn-primary btn-sm">
                <i class="bi bi-cart4"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 放大圖片 Modal -->
  <div v-if="zoomImg" @click="closeZoom"
     style="position:fixed;top:0;left:0;width:100%;height:100%;
            background:rgba(0,0,0,0.7);display:flex;justify-content:center;
            align-items:center;cursor:pointer;z-index:9999;">
  <img :src="zoomImg" style="height:500px; width:auto;">
</div>
</template>

<style scoped>
img {
  width: 100%;
  height: 300px;
  background: rgb(255, 254, 254);
}
.card-body {
  background: rgb(241, 241, 241);
}
.row-cols-1 {
  padding: 100px;
}
.card-text {
  margin: 12px;
}
.row {
  padding-top: 180px;
}
.apple1 {
  padding-top: 150px;
}
</style>
