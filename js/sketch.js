var cnv;

var cX, cY;

function setup() {
	cnv = createCanvas(300, 300);
	cnv.parent('sketch');

	var centerX = width/2;
	var centerY = height/2;

	cX = centerX;
	cY = centerY;

	background(0);
  ellipse(mouseX, mouseY, 80, 80);
}

function draw() {
	background(0);

  ellipse(mouseX, mouseY, 80, 80);
}
