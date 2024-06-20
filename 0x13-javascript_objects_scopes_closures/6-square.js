#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else if (c !== undefined) {
      let sq = '';
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) {
          sq += c;
        }
        if (i !== this.height) {
          sq += '\n';
        }
      }
      console.log(sq);
    }
  }
}
module.exports = Square;
