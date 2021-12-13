#!/usr/bin/node

const process = require('process')
let args = process.argv

if (args.lenght === 0) console.log("No argument")
if (args.lenght === 1) console.log("Argument found")
else {
  console.log("Arguments found")
}
