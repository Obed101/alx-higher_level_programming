#!/usr/bin/node

let iterator = 1;
let argument = Number(process.argv[2]);
if (argument !== NaN){
  while (iterator <= argument){
    console.log('C is fun');
    iterator++;
  }
} else {
    console.log('Missing number of occurrences');
}
