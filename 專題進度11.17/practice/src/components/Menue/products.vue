<script setup>
import product_item from './product_item.vue';

</script>


<template>
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">特殊傳說Ⅲ vol.09</h5>
        <p class="card-text">原定價: 299元</p>
        <p class="card-text">庫存: 3</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
</div>


<product_item/>


</template>

<style scoped>
img{
  width: 100%;
  height: 300px;
  background: rgb(255, 254, 254);
}
.card-body{
  background: rgb(241, 241, 241);

}
.row-cols-1{
  padding: 100px;
}
.card-text{
  margin: 12px;
}

.row{
  padding-top: 180px;
}

</style>