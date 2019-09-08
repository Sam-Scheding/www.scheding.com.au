<template>
  <div class="d-flex justify-content-center" id="p5Canvas"></div>
</template>

<script>
import run from './script.js';
import P5 from 'p5';

export default {
  name: 'Canvas',
  props: {
    bg: {
      type: String,
      default: '#000000',
    },
    color: {
      type: String,
      default: '#009600', // Green
    },
    horizon: {
      type: Number,
      default: 200,
    },
    thickness: {
      type: Number,
      default: 2,
    },
    speed: {
      type: Number,
      default: 3,
    },
  },
  mounted() {
    const config = {
      BG: this.bg,
      COLOR: this.color,
      HORIZON: this.horizon,
      THICKNESS: this.thickness,
      SPEED: this.speed,
    };
    run(config);
  },
}

</script>
