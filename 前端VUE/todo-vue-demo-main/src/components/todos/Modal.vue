<script setup>
import { useTemplateRef } from 'vue';

function openModal() {
  const dialog = useTemplateRef('dialog')
  dialog.showModal()
}

defineExpose({ openModal })
</script>

<template>
  <dialog ref="dialog" class="modal">
    <div class="modal-box">
      <h3 class="text-lg font-bold">更新</h3>
      <p class="py-4">
        <input type="text" class="input w-full">
      </p>
      <div class="modal-action">
        <form method="dialog" class="flex gap-2">
          <a href="#" class="btn btn-success">更新</a>
          <button class="btn">取消</button>
        </form>
      </div>
    </div>
  </dialog>
</template>
