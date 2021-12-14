#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let cp = c;
    if (!c) {
      cp = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(cp.repeat(this.size));
    }
  }
}

module.exports Square;
