#!/usr/bin/node

// adds two integers
const firstNum = parseInt(process.argv[2], 10);
const secondNum = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}
console.log(add(firstNum, secondNum));
