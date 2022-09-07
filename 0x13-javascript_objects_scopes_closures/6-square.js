#!/usr/bin/node
const baseSquare = require('./5-square');

module.exports = class Square extends baseSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
};
