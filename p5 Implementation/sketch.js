let totalDigits = 4;
// total number of digits to be approximated 

let totalIterationBetweenFrames = 1000;
// total iteration between frames to avoid deviating from the actual velocity
// TODO: Find a way to avoid looping a billion times between each frames

let body1 = new Body(Math.pow(100, totalDigits - 1), 100, 300, -2 / totalIterationBetweenFrames);
let body2 = new Body(1, 30, 30, 0);
// initializing the bodies 

let totalCollision = 0;
// the number of collisions 

function setup() {
  createCanvas(1000, 400);
  // setting up canvas 
}

function draw() {
  background(0);
  // updating background 

  for (let i = 0; i < totalIterationBetweenFrames; i++) {
    body1.collisionHandle(body2);
    // handling collision 

    if (body2.isCollidingWall() || body2.isColliding(body1)) {
      totalCollision++;
    }
    // updating collision 

    body1.update();
    body2.update();
    // updating both the bodies 
  }

  body1.render();
  body2.render();
  // rendering bodies 

  if((body1.velocity > 0 && body2.velocity > 0 && body1.velocity > body2.velocity) || (body2.velocity == body1.velocity)){
    noLoop();
    print(totalCollision);
  }
  // exiting out the loop when the approximation is complete 
}
