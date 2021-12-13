#!/usr/bin/node

import { argv } from 'process';
let converted = Number(argv[1]);
if (converted === NaN){
    console.log('Not a number');
} else {
    console.log('My number: '+ converted);
}
