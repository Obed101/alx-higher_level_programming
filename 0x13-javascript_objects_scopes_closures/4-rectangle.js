#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (!w || !h) {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    temp = this.height;
    this.height = this.width;
    this.width = temp;
    temp = null;
  }
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
