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

  print () {
    let rectangle = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        rectangle += 'X';
      }
      if (i !== this.height) {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }
}
module.exports = Rectangle;
