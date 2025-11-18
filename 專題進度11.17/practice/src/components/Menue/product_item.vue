<template>
  <div class="card mx-auto my-3" style="width: 70%;">
    <div class="d-flex">

      <!-- 商品圖片 -->
      <img src="..." style="width: 40%; object-fit: cover;" alt="...">

      <!-- 右側內容整塊 -->
      <div class="flex-grow-1">

        <!-- 文字區 -->
        <div class="card-body">
          <h5 class="card-title">特殊傳說Ⅲ vol.09</h5>
          <p class="card-text">作者: 護玄</p>
          <p class="card-text">出版社: 蓋亞文化</p>
          <p class="card-text">出版日期: 2024/10/16</p>
          <p class="card-text">原定價: 299元</p>
          <p class="card-text">ISBN: 9786263841253</p>
          <p class="card-text">庫存: 3</p>
          <p class="card-text">銷售量: 10</p>
        </div>
      </div>
    </div>

    <!-- 商品販售狀態 -->
    <div class="pt-5">
        <table class="table">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">賣家</th>
                <th scope="col">幾成新</th>
                <th scope="col">有無筆記</th>
                <th scope="col">書況</th>
                <th scope="col">二手價</th>
                <th scope="col">購買</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>貓咪賣家</td>
                <td>六成新</td>
                <td>有</td>
                <td>有泡過水</td>
                <td>100元</td>
                <td><button class="btn btn-primary btn-sm"><i class="bi bi-cart4"></i></button></td>     
                </tr>
            </tbody>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>貓咪賣家</td>
                <td>六成新</td>
                <td>有</td>
                <td>有泡過水</td>
                <td>100元</td>
                <td><button class="btn btn-primary btn-sm"><i class="bi bi-cart4"></i></button></td>     
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>

<style scoped>
img{
  width: 100%;
  height: 300px;
  background: rgb(189, 188, 188);
}


.col-span {
width: 20%;   /* 每欄 20% */
}
.col-price {
width: 15%;
}
.col-btn {
width: 25%;
text-align: right;
}


/* table.table tbody tr:last-child th,
table.table tbody tr:last-child td {
    border-bottom: none;
} */
</style>