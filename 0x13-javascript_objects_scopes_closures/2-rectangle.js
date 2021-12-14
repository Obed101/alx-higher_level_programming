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
}
modules.exports = Rectangle;
