#!/usr/bin/node
const array = process.argv.slice(2);
if (array.length === 0 || array.length < 2) {
  console.log('0');
} else {
  let largest = array[0];
  let secondLargest = array[0];
  let i = 1;
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
