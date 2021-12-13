#!/usr/bin/node

let converted = Number(process.argv[1]);
if (converted) {
    console.log('My number: '+ converted);
} else {
    console.log('Not a number');
}
