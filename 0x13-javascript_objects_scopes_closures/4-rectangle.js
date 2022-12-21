#!/usr/bin/node

// class Rectangle that defines a rectangle:
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this.prototype;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // prints the shape of Rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += 'X';
      }
      console.log(shape);
    }
  }

  // Rotates the Rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Double the value of the width and height
  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
