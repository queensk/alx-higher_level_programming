#!/usr/bin/node

// class Rectangle that defines a rectangle:
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.width = 0;
      this.hight = 0;
    } else {
      this.width = w;
      this.hight = h;
    }
  }
};
