#!/usr/bin/node

// Increment the value of an object
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};
console.log(myObject);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
