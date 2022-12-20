#!/usr/bin/node

// Use the map function to create a new list
// list, multiples by the index in the list
const { list } = require('./100-data.js');

const newList = list.map((x, i) => x * i);
console.log(list);
console.log(newList);
