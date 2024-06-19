#!/usr/bin/node
if (isNaN(Number(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let sq = '';
  const size = process.argv[2];
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      sq += 'X';
    }
    if (x !== size - 1) {
      sq += '\n';
    }
  }
  console.log(sq);
}
