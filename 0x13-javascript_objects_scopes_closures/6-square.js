#!/usr/bin/node
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint (c) {
    let row;
    let i;
    const character = c || 'X';
    row = '';
    for (i = 0; i < this.width; i++) {
      row += character;
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
