#!/usr/bin/node

// Import the dictionary from the file 101-data.js
const { dict } = require('./101-data.js');

// Create an empty dictionary to store the user ids by occurrence
const newDict = {};

// Iterate over the entries in the dictionary
for (const [userId, occurrence] of Object.entries(dict)) {
  // If the occurrence is not already a key in the new dictionary, add it as a key with an empty value
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  // Add the user id to the list of user ids for this occurrence
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
