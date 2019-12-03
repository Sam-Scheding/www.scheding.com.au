<template>
  <a
    class="root"
    v-bind:href="href"
  >
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: 'Anchor',
  props: {
    href: {
      type: String,
      default: '#',
    }
  }
}
</script>

<style lang="css" scoped>
  .root {
    text-decoration: none;
    color: #F0F0F0;
    text-transform: uppercase;
  }

  .root:hover {
    text-decoration: underline;
  }
</style>
