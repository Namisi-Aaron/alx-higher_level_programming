#!/usr/bin/node
const times = parseInt(process.argv[2]);
if ((process.argv[2] === undefined) || (isNaN(times))) {
  console.log('Missing number of occurrences');
}
let i = 0;
for (; i < times; i++) {
  console.log('C is fun');
}
