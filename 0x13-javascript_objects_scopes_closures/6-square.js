#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    }
  }
}

module.exports Square;
