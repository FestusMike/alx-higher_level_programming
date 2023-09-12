#!/usr/bin/node

/*
class Rectangle that defines a rectangle
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const widthNew = this.height;
    const heightNew = this.width;
    this.width = widthNew;
    this.height = heightNew;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
