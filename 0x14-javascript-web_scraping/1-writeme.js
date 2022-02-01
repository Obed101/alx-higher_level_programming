#!/usr/bin/node
// This js code writes into a txt file
const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[2], arg[3], 'utf-8', (err) => {
if (err) throw err;
});
