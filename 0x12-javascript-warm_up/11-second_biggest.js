#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const array = args.map(str => +str);
  const newArray = array.filter(num => num !== Math.max(...array));
  console.log(Math.max(...newArray));
}
