import P5 from 'p5';
import LineSystem from './line_system.js';

const script = (sketch) => {

  // If no config has been set, load the default config
  !!sketch.config ? sketch.config : sketch.config = {
    BG: 'pink',
    COLOR: '#000000',
    HORIZON: 0,
    THICKNESS: 3,
    SPEED: 2,
    WIDTH: window.innerWidth,
    HEIGHT: window.innerHeight,
    LINES: 10,
  };
  let points = [];
  let ls;

  sketch.setup = () => {
    sketch.createCanvas(sketch.config['WIDTH'], sketch.config['HEIGHT']);
    points.push(createPoint());
    points.push(createPoint());
    points.push(createPoint());
    ls = new LineSystem();

  }

  sketch.draw = () => {
    sketch.background(sketch.config['BG']);
    for(let idx = 0; idx < points.length; idx++){
      let curr = points[idx];
      let next = points[(idx + 1) % points.length];
      // line(curr.pos.x, curr.pos.y, next.pos.x, next.pos.y);
      ls.addLine(curr.pos, next.pos);
    }
    ls.run(sketch);
    points.forEach((p) => { p.update(); });
  }

  const createPoint = () => {

    return {
      pos: {
        x: sketch.random(0, sketch.config['WIDTH']),
        y: sketch.random(0, sketch.config['HEIGHT']),
      },
      vel: {
        x: sketch.random([-4, -3, 3, 4]),
        y: sketch.random([-4, -3, 3, 4]),
      },
      update() {
        if(0 >= this.pos.x || this.pos.x >= sketch.config['HEIGHT']){ this.vel.x *= -1; }
        this.pos.x += this.vel.x;
        if(0 >= this.pos.y || this.pos.y >= sketch.config['WIDTH']){ this.vel.y *= -1; }
        this.pos.y += this.vel.y;
      },
      draw() {
        sketch.stroke(255);
        sketch.strokeWeight(8);
        sketch.point(this.pos.x, this.pos.y);
      },
    };
  }
}

export default script;
