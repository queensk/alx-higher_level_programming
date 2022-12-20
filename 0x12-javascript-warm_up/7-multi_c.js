#!/usr/bin/node

// prints x times c is fun
const arg = process.argv[2];

if (/^-?\d+$/.test(arg)) {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
