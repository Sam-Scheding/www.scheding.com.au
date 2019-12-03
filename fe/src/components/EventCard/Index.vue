<template>
  <div class="root">
    <img
      v-bind:src="event.img"
      class="img"
    >
    <div class="title">
      <a
        v-bind:href="event.url"
        target="_blank"
        class="content"
        >
        {{ event.title }}
      </a>
    </div>
    <p class="tag">{{ event.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'EventCard',
  props: {
    event: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>

.root {
  box-shadow: rgba(60,64,67,.3) 0 1px 2px 0, rgba(60,64,67,.15) 0 1px 3px 1px;
  background: #FAFAFA;
  max-width: 380px;
  margin-left: 20px;
  margin-right: 20px;
  transition: all .2s ease-in-out;
}
.img {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 200px;
  width: 100%;
}

.footer {
  font-size: 10px;
  border-top: 1px solid #CCC;
  color: #808285;
  width: 100%;
}

.content {
  color: #202020;
  text-transform: uppercase;
  font-size: 12px;
  padding: 10 0 10 10;
}
</style>
