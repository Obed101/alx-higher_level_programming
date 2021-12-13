#!/usr/bin/node
// finding the first runner up
const size = process.argv.length;
if (size < 4) {
  console.log('0');
} else {
  const biggest = process.argv.slice(2);

  biggest.sort((x, y) => y - x);
  console.log(big[1]);
}
