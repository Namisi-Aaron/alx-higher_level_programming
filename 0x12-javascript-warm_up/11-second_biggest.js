#!/usr/bin/node
const array = process.argv.slice(2).map(Number);
if (array.length === 0 || array.length < 2) {
  console.log(0);
} else {
  let largest = Math.max(array[0], array[1]);
  let secondLargest = Math.min(array[0], array[1]);
  let i = 2;
  for (; i < array.length; i++) {
    if (array[i] > largest) {
      secondLargest = largest;
      largest = array[i];
    } else if ((array[i] > secondLargest) && (array[i] !== largest)) {
      secondLargest = array[i];
    }
  }
  console.log(secondLargest);
}
