#!/usr/bin/node
// This file is reading the content of a txt file
const request = require('request');
const url = process.argv[2];
const method = 'GET';

request(url, method, (err, data, body) => {
  console.log(`code: ${response.statuscode}`)
  if (err) console.log(err);
});
