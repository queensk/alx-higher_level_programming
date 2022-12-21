#!/usr/bin/node

const fs = require('fs');

// get file path form the scripts arguments
const filePathOne = process.argv[2];
const filePathTwo = process.argv[3];
const destination = process.argv[4];

// read content of the files
const dataFileOne = fs.readFileSync(filePathOne, 'utf8');
const dataFileTwo = fs.readFileSync(filePathTwo, 'utf8');
const concatData = dataFileOne + dataFileTwo;

fs.writeFileSync(destination, concatData);
