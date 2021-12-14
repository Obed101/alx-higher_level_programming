#!/usr/bin/node
const Square1 = require('./5square')
class Square extends Square1 {
  constructor (size) {

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
}
