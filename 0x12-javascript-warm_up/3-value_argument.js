#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Print the first argument of message if no argument is not found
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
