#!/usr/bin/node
const process = require('process');

let iterator = 1;
let argument = Number(process.argv[1]);
if (argument !== NaN){
  while (iterator <= argument){
    console.log('C is fun');
  }
} else {
    console.log('Missing number of occurrences');
}
