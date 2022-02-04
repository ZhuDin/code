function Shape() {}

Shape.prototype.X = 0;
Shape.prototype.Y = 0;

Shape.prototype.move = function (x, y) {
    this.X = x;
    this.Y = y;
}

Shape.prototype.distance_from_origin = function() {
    return Math.sqrt(this.X * this.X + this.Y * this.Y);
}

Shape.prototype.area = function() {
    throw new Error("I don't have a form yet");
}

function Square() {}

Square.prototype = new Shape();
Square.prototype.__proto__ = Shape.prototype;
Square.prototype.Width = 0;
Square.prototype.area = function() {
    return this.Width * this.Width;
}

let sq = new Square();
sq.move(-5, -5);
sq.Width = 5;
console.log(sq.area());
console.log(sq.distance_from_origin());