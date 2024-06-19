#!/usr/bin/node
const list = [];
exports.logMe = function (item) {
  console.log(`${list.length}: ${item}`);
  list.push(item);
};
