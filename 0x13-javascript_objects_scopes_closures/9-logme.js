#!/usr/bin/node

// function that prints the number of arguments already printed
// and the new argument value. (see example below)

exports.logMe = function (item) {
    let count = 0;
    return function (item) {
      console.log(`${count}: ${item}`);
      count++;
    }
  }
  