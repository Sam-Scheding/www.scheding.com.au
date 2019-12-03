<template>
  <div class="root">
    <Nav />
    <Today />
  </div>
</template>

<script>
import Nav from '../Nav/Index.vue';
import Today from '../Today/Index.vue';

export default {
  name: 'Root',
  components: {
    Nav,
    Today,
  },
}
</script>

<style scoped>
  .root {
    border: 1px solid red;
    background-color: #202020;
  }
</style>
