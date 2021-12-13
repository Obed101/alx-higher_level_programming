#!/usr/bin/node

const count = argv.lenght;

if (count === 1) {
  console.log('No argument');
} else if (count === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
