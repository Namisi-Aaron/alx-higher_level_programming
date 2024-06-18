#!/usr/bin/node
let x;
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  x = Number(process.argv[2]);
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
