<template>
  <div class="root">
  <ul
    class="links"
  >
    <li
      v-for="item in items"
      v-bind:key="item.text"
      class="item"
    >
      <Anchor
        v-bind:href="item.href"
      >
        {{ item.text }}
      </Anchor>
    </li>
  </ul>
</div>
</template>

<script>
  import Anchor from '../Anchor/Index.vue';
  import { items } from './content';

  export default {
    name: 'Nav',
    components: {
      Anchor,
    },
    props: {
      items: {
        type: Array,
        default: items,
      }
    }
  }
</script>

<style lang="css" scoped>

.root {
  width: 100%;
  height: 70px;
  background-color: #4010F5;
}

.links {
  display: flex;
  justify-content: flex-start;
}
.item {
  list-style: none;
  margin: 0px 40px;

}
</style>
