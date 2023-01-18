#!/usr/bin/node

// Get the number of arguments passed on to the script

const numArgs = process.argv.length - 2;

// print argument on passing arguments or No argument

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
