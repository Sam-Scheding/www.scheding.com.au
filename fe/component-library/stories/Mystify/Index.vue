<template>
  <div class="d-flex justify-content-center" id="p5-canvas-mystify"></div>
</template>

<script>
import script from './sketch.js';
import P5 from 'p5';

export default {
  name: 'Canvas',
  props: {
    id: {
      type: String,
      default: 'p5-canvas-mystify',
    },
    width: {
      type: Number,
      default: 500,
    },
    height: {
      type: Number,
      default: 500,
    },
    lines: {
      type: Number,
      default: 10,
    },
    bg: {
      type: String,
      default: '#000000',
    },
    color: {
      type: String,
      default: '#009600', // Green
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
  created() {
    if (window.p5 && p5.instance) {
        p5.instance.remove();
        p5.instance = window.setup = window.draw = null;
    } else {
        const canv = document.querySelector('canvas');
        canv && canv.remove();
    }
    const config = {
      BG: this.bg,
      WIDTH: this.width,
      HEIGHT: this.height,
      LINES: this.lines,
      COLOR: this.color,
      HORIZON: this.horizon,
      THICKNESS: this.thickness,
      SPEED: this.speed,
    };
    let sketch = new P5(script);
    sketch.config = config;
  },
}

</script>
