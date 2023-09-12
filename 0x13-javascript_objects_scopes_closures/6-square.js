#!/usr/bin/node

/*
 class Square that defines a square and inherits from Square of 5-square.js
*/

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log((c.repeat(this.width)));
    }
  }
};
