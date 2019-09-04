const HORIZON = 0;

const Line = (x1, y1, x2, y2, vel, lifespan) => {
  return {
    p1: { x: x1, y: y1 },
    p2: { x: x2, y: y2 },
    vel: vel,
    lifespan: lifespan,
    update() {
      if(lifespan){
        this.p1.y += vel * (100 - this.lifespan) * 0.01;
        this.p2.y += vel * (100 - this.lifespan) * 0.01;
        this.lifespan -= 1;
      }
    },
  }
};

const LineSystem = () => {
    return {
      lines: [],
      add(l) {
        this.lines.push(l);
      }
    }
};

const ls = LineSystem();

const script = function (p5) {

  p5.setup = () => {
    p5.createCanvas(window.innerWidth, window.innerHeight);
    p5.strokeWeight(3);
    ls.add(Line(0, HORIZON, window.innerWidth, HORIZON, 0, undefined));
    ls.add(Line(1*window.innerWidth/10, HORIZON, -3*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(2*window.innerWidth/10, HORIZON, -1*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(3*window.innerWidth/10, HORIZON, 1*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(4*window.innerWidth/10, HORIZON, 3*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(5*window.innerWidth/10, HORIZON, 5*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(6*window.innerWidth/10, HORIZON, 7*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(7*window.innerWidth/10, HORIZON, 9*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(8*window.innerWidth/10, HORIZON, 11*window.innerWidth/10, window.innerHeight, 0));
    ls.add(Line(9*window.innerWidth/10, HORIZON, 13*window.innerWidth/10, window.innerHeight, 0));

  };

  p5.draw = () => {
    p5.background(0);

    const frame = p5.frameCount;
    if(frame % 30 === 0){
      ls.add(Line(0, HORIZON, window.innerWidth, HORIZON, 2, 100));
    }

    ls.lines.forEach((l) => {
      l.update();
      p5.stroke(p5.color(0, 150, 0));
      p5.line(l.p1.x, l.p1.y, l.p2.x, l.p2.y);
    });
  };
};

export default script;
