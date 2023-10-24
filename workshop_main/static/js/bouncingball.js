var canvas = {
	element: document.getElementById('background_canvas'),
	width: 300,
	height: 90,
	initialize: function () {
		this.element.style.width = this.width + 'px';
		this.element.style.height = this.height + '%';

		document.body.appendChild(this.element);
	}
};

var Ball = {
	create: function (color, dx, dy, width, height) {
		var newBall = Object.create(this);
		newBall.dx = dx;
		newBall.dy = dy;
		newBall.width = width;
		newBall.height = height;
		newBall.element = document.createElement('div');
		newBall.element.style.background = color;
		newBall.element.style.width = newBall.width + 'px';
		newBall.element.style.height = newBall.height + 'px';
		newBall.element.className += ' ball';
		newBall.width = parseInt(newBall.element.style.width);
		newBall.height = parseInt(newBall.element.style.height);
		canvas.element.appendChild(newBall.element);
		return newBall;
	},
	moveTo: function (x, y) {
		this.element.style.left = x + 'px';
		this.element.style.top = y + '%';
	},
	changeDirectionIfNecessary: function (x, y) {
		if (x <= 0 || x >= canvas.width) {
			this.dx = -this.dx;
		}
		if (y <= 0 || y >= canvas.height) {
			this.dy = -this.dy;
		}
	},
	draw: function (x, y) {
		this.moveTo(x, y);
		var ball = this;

		function animate() {
			ball.changeDirectionIfNecessary(x, y);
			x += ball.dx;
			y += ball.dy;
			ball.moveTo(x, y);
			requestAnimationFrame(animate);
		}

		animate();
	}

};
canvas.initialize();

// 파란색을 나중에 배치하니 파란색이 다 위를 덮고 있어서 섞이도록 함

// 보라색공
var ball1 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 1, 0.2, 220, 220);

// 파란색공
var ball2 = Ball.create("linear-gradient(180deg, #86FFD3 0%, #84FAE3 30.73%, #83F6EE 52.6%, #81F0FF 100%)", 1, 0.2, 220, 220);

// 보라색공
var ball3 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 1, 0.2, 220, 220);

// 보라색공
var ball4 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 1, 0.2, 220, 220);

// 파란색공
var ball5 = Ball.create("linear-gradient(180deg, #86FFD3 0%, #84FAE3 30.73%, #83F6EE 52.6%, #81F0FF 100%)", 1, 0.2, 220, 220);

// 보라색공
var ball6 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 1, 0.2, 220, 220);

// 파란색공
var ball7 = Ball.create("linear-gradient(180deg, #86FFD3 0%, #84FAE3 30.73%, #83F6EE 52.6%, #81F0FF 100%)", 1, 0.2, 220, 220);

ball1.draw(100, 80);
ball2.draw(200, 90);
ball3.draw(10, 10);
ball4.draw(280, 50);
ball5.draw(30, 40);
ball6.draw(100, 20);
ball7.draw(60, 10);