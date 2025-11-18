<script setup>
import { ref, computed } from 'vue';

// 購物車資料，每個商品帶 seller 屬性
var cart = ref([
  { name: '貓咪去旅行', price: 300, seller: '貓賣家' },
  { name: '123木頭人', price: 200, seller: '貓賣家' },
  { name: '我們這一家', price: 250, seller: '狗賣家' }
]);

// 分組：依賣家分組
var groupedCart = computed(() => {
  const groups = {};
  cart.value.forEach(item => {
    if (!groups[item.seller]) {
      groups[item.seller] = [];
    }
    groups[item.seller].push(item);
  });
  return groups;
});

// 每個賣家的小計
function sellerSubtotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// 總金額
var total = computed(() => cart.value.reduce((sum, item) => sum + item.price, 0));

// 面交地點資料（每個賣家一個）
var locations = ref({});

// 控制是否顯示確認頁
var showCheckoutConfirm = ref(false);

// 刪除商品
function removeItem(index) {
  cart.value.splice(index, 1);
}

// 前往結帳
function checkout() {
  // 初始化每個賣家的面交地點
  Object.keys(groupedCart.value).forEach(seller => {
    if (!locations.value[seller]) locations.value[seller] = '';
  });
  showCheckoutConfirm.value = true;
}

// 確認結帳
function confirmCheckout() {
  // 檢查每個賣家面交地點
  for (const seller of Object.keys(groupedCart.value)) {
    if (!locations.value[seller]) {
      alert(`請選擇 ${seller} 的面交地點！`);
      return;
    }
  }
  let message = `結帳成功！\n\n`;
  for (const seller of Object.keys(groupedCart.value)) {
    message += `${seller} 小計 $${sellerSubtotal(groupedCart.value[seller])}，面交地點：${locations.value[seller]}\n`;
  }
  message += `\n總金額 $${total.value}`;
  alert(message);

  // 清空購物車
  cart.value = [];
  showCheckoutConfirm.value = false;
  locations.value = {};
}
</script>

<template>
  <div class="cart-container">
    <!-- 購物車清單 -->
    <div v-if="!showCheckoutConfirm">
      <h2>購物車內容</h2>

      <div v-for="(item, i) in cart" :key="i" class="cart-item">
        <div class="cart-name">{{ item.name }}（{{ item.seller }}）</div>
        <div class="cart-price">二手價 ${{ item.price }}</div>
        <button class="btn-delete" @click="removeItem(i)">刪除</button>
      </div>

      <div class="cart-summary">
        <div>總金額：${{ total }}</div>
      </div>

      <button class="btn-checkout" @click="checkout">前往結帳</button>
    </div>

    <!-- 訂單確認 -->
    <div v-else>
      <h2>訂單確認</h2>

      <div v-for="(items, seller) in groupedCart" :key="seller" class="seller-block">
        <h3>{{ seller }}</h3>

        <div v-for="(item, i) in items" :key="i" class="cart-item">
          <div class="cart-name">{{ item.name }}</div>
          <div class="cart-price">二手價 ${{ item.price }}</div>
        </div>

        <div class="cart-summary">
          小計：${{ sellerSubtotal(items) }}
        </div>

        <div class="location-input">
          <label>面交地點：</label>
          <input type="text" v-model="locations[seller]" placeholder="輸入面交地點" />
        </div>

        <hr />
      </div>

      <div class="cart-summary">
        總金額：${{ total }}
      </div>

      <button class="btn-checkout" @click="confirmCheckout">立即結帳</button>
    </div>
  </div>
</template>

<style scoped>
.cart-container {
  width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: white;
}

.cart-item {
  padding: 5px 0;
}

.cart-name {
  font-weight: 500;
}

.cart-price {
  color: gray;
  font-size: 14px;
  margin-top: 3px;
}

.btn-delete {
  color: red;
  margin-top: 5px;
  background: none;
  border: none;
  cursor: pointer;
}

.cart-summary {
  text-align: right;
  font-weight: bold;
  margin-top: 10px;
}

.location-input {
  margin-top: 5px;
}

.location-input input {
  width: 100%;
  padding: 5px;
  margin-top: 3px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.btn-checkout {
  width: 100%;
  margin-top: 10px;
  padding: 8px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-checkout:hover {
  background: #0069d9;
}

hr {
  margin: 10px 0;
}
</style>