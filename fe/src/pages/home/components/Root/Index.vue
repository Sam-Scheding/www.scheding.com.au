<script>
import navigationLinks from './navigationLinks';

export default {
  name: 'Root',
  computed: {
      links: () => {
        return navigationLinks;
      }
  }
}
</script>

<template>
  <ul>
    <li
      v-for="link in links"
      v-bind:key="link.label"
    >
      <a v-bind:href="link.href">{{ link.label }}</a>
    </li>
  </ul>

</template>

<style scoped>
  .root {
    border: 1px solid red;
    background-color: #202020;
  }
</style>
