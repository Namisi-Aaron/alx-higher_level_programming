#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || !width || !height) {
      return;
    } else {
      this.width = width;
      this.height = height;
    }
  }
}
module.exports = Rectangle;
