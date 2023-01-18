#!/usr/bin/node

// class Rectangle that defines a rectangle:
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this.Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
