#!/usr/bin/node
let i, j;
let string = '';
const character = 'X';
const size = parseInt(process.argv[2]);
if ((process.argv[2] === undefined) || (isNaN(size))) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      string += character;
    }
    if (i !== size - 1) {
      string += '\n';
    }
  }
  console.log(string);
}
