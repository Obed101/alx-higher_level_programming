#!/usr/bin/node

const process = require('process')
let args = process.argv

if (args[2] === 0) console.log("No argument")

else {
  console.log(args[2])
}
