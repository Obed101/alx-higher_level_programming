#!/usr/bin/node
// This js code writes into a txt file
const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[1], arg[2], 'utf-8', (err) => {
if (err) throw err;
});
