#!/usr/bin/node

// class Square that defines a square and inherits from Square of 5-square.js

const Square = require('./5-square');
module.exports = class Square extends Square {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
