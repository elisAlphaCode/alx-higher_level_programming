#!/usr/bin/node
// Import the base class: Rectangle
const Rectangle = require('./4-rectangle');

// subclasses base class
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
