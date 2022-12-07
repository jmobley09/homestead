<script setup lang="ts">
const router = useRouter();
const errorCode = ref<number>(404);
const back = () => {
  router.push({ name: "Home" });
};
</script>

<template>
  <div class="bg-base-100 flex flex-col items-center gap-20 py-20">
    <div class="card bg-base-100 w-96">
      <div class="card-body">
        <h2 class="card-title">
          Error {{ errorCode }}!
        </h2>
        <p>We're sorry, something is not right, page not found!</p>
        <div class="card-actions justify-end">
          <button class="btn-primary btn" @click="back">
            Back !
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
