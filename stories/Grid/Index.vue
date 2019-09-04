<template>
  <div class="d-flex justify-content-center" id="p5Canvas"></div>
</template>

<script>
import script from './script.js';
export default {
  name: 'Canvas',
  props: {
    backgroundColour: {
      required: true,
    },
  },
  mounted() {
    const P5 = require('p5');
    new P5(script)
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #p5Canvas {
  }
</style>
