#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const wCopy = this.width;
    this.width = this.height;
    this.height = wCopy;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
