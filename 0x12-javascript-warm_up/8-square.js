#!/usr/bin/node
let size;
let square = '';
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  size = Number(process.argv[2]);

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
      }
      if (i < size - 1) {
        square += '\n';
      }
    }
}
console.log(square);
