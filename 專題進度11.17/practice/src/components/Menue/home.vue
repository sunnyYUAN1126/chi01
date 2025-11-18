<script setup>
import product from './products.vue';

</script>

<template>
  <nav class="navbar bg-body-tertiary  navbar-expand-lg bg-body-tertiary fixed-top second-nav">
    <div class="container-fluid">
      <a class="navbar-brand">Let's go~</a>


    <ul class="nav nav-pills">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#">ALL</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">語言</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">社會</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">理工</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">自然</a>
      </li>
    </ul>          
    

    <form class="d-flex" role="search">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
      <button class="btn btn-outline-success" type="submit">
        <i class="bi bi-search"></i>
      </button>
    </form>

    </div>
  </nav>

  <product/>

             



</template>


<style scoped>
.nav-link {
  color: rgb(0, 0, 0) !important;
}
.active{
  background: rgb(216, 210, 211) !important;
}
.nav-link:hover {
  background-color: rgb(216, 210, 211) !important; /* 可改成喜歡的顏色 */
  color: rgb(0, 0, 0) !important;
  font-weight: bold;
}


.second-nav {
  top: 80px;  /* 第一個 nav 的高度 */
}


</style>

