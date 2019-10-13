import P5 from 'p5';

const script = (sketch) => {
  !!sketch.config ? sketch.config : sketch.config = {
    BG: 'pink',
    COLOR: '#000000',
    HORIZON: 0,
    THICKNESS: 3,
    SPEED: 2,
  };

  let ls;

  const Line = (x1, y1, x2, y2, vel, lifespan) => {
    return {
      p1: { x: x1, y: y1 },
      p2: { x: x2, y: y2 },
      vel: vel,
      age: lifespan,
      lifespan: lifespan,
      update() {
        if(lifespan){
          this.p1.y += vel * (this.age - this.lifespan) * 0.01;
          this.p2.y += vel * (this.age - this.lifespan) * 0.01;
          this.lifespan -= 1;
        }
      },
      isDead() {
        // Some lines are immortal, so if lifespan is undefined, don't delete them
        return this.lifespan && this.lifespan <= 0;
      }
    }
  };

  const LineSystem = () => {
      return {
        lines: [],
        add(l) { this.lines.push(l); }
      }
  };

  sketch.setup = () => {
    sketch.createCanvas(window.innerWidth, window.innerHeight);
    sketch.strokeWeight(sketch.config['THICKNESS']);
    ls = LineSystem();
    // pos is the horizontal spacing of the 'vertical' lines. They need to be
    // further from eachother at the bottom than att the top to create the
    // vanishing point effect
    const pos = [
      {x1: 1, x2: -3},
      {x1: 2, x2: -1},
      {x1: 3, x2: 1},
      {x1: 4, x2: 3},
      {x1: 5, x2: 5},
      {x1: 6, x2: 7},
      {x1: 7, x2: 9},
      {x1: 8, x2: 11},
      {x1: 9, x2: 13},
    ];
    ls.add(Line(0, sketch.config['HORIZON'], window.innerWidth, sketch.config['HORIZON'], 0, undefined));

    pos.forEach(p => {
      ls.add(Line(p.x1*window.innerWidth/10, sketch.config['HORIZON'], p.x2*window.innerWidth/10, window.innerHeight, 0, undefined));
    });
  };

  sketch.draw = () => {

    sketch.background(sketch.config['BG']);
    const frame = sketch.frameCount;

    if(frame % 30 === 0){ // Add a new horizontal line every 30 frames
      ls.add(Line(0, sketch.config['HORIZON'], window.innerWidth, sketch.config['HORIZON'], sketch.config['SPEED'], 400));
    }
    let toDelete;
    ls.lines.forEach((l) => {
      if(l.isDead()){ toDelete = l; }
      l.update();
      sketch.stroke(sketch.config['COLOR']);
      sketch.line(l.p1.x, l.p1.y, l.p2.x, l.p2.y);
    });
    var index = ls.lines.indexOf(toDelete);
    if (index !== -1) ls.lines.splice(index, 1);
  };

};

export default script;
