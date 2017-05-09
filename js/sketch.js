var cnv;

var cX, cY;

function centerCanvas() {
  var x = (windowWidth - width) / 2;
  var y = (windowHeight - height) / 2;
  cnv.position(x, y);
}

function setup() {
	cnv = createCanvas(300, 300);
	cnv.parent('post-content');
	centerCanvas()

	var centerX = width/2;
	var centerY = height/2;

	cX = centerX;
	cY = centerY;
	background(0);
  ellipse(mouseX, mouseY, 80, 80);
}

function draw() {
	centerCanvas()
	background(0);

  ellipse(mouseX, mouseY, 80, 80);
}
