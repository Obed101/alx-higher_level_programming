#!/usr/bin/node

const process = require('process');
const count = process.argv.lenght;

if (count === 1) {
  console.log('No argument');
} else if (count === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
