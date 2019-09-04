<template>
  <div class="d-flex justify-content-center" id="p5Canvas"></div>
</template>

<script>
import script from './script.js';
export default {
  name: 'Canvas',
  props: {
  },
  mounted() {
    const P5 = require('p5');
    new P5(script)
  }
}
</script>
