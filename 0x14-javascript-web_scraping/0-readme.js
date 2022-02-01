#!/usr/bin/node
// This file is reading the content of a txt file
const fs = require('fs');
const myArgs = process.argv;
fs.readFile(myArgs[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
