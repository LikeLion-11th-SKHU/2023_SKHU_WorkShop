var canvas = {
    element: document.getElementById('background_canvas'),
    width: 700,
    height: 812,
    initialize: function () {
        this.element.style.width = this.width + 'px';
        this.element.style.height = this.height + 'px';
        
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
        this.element.style.top = y + 'px';
    },
    changeDirectionIfNecessary: function (x, y) {
        if (x < 0 || x > canvas.width - this.width) {
            this.dx = -this.dx;
        }
        if (y < 0 || y > canvas.height - this.height) {
            this.dy = -this.dy;
        }
    },
    draw: function (x, y) {
        this.moveTo(x, y);
        var ball = this;
        setTimeout(function () {
            ball.changeDirectionIfNecessary(x, y);
            ball.draw(x + ball.dx, y + ball.dy);
        }, 1000 / 60);
    }
};
canvas.initialize();
// 보라색공
var ball1 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 2, 6, 180, 180);
var ball2 = Ball.create("linear-gradient(180deg, #FF87E5 29.69%, #DA81F0 52.08%, #AC79FF 79.69%)", 4, 5, 280, 280);
// 파란색공
var ball3 = Ball.create("linear-gradient(180deg, #86FFD3 0%, #84FAE3 30.73%, #83F6EE 52.6%, #81F0FF 100%)", 2, 2, 260, 260);
var ball4 = Ball.create("linear-gradient(180deg, #86FFD3 0%, #84FAE3 30.73%, #83F6EE 52.6%, #81F0FF 100%)", 4, 6, 180, 180);
ball1.draw(70, 0);
ball2.draw(350, 330);
ball3.draw(100, 300);
ball4.draw(500, 100);