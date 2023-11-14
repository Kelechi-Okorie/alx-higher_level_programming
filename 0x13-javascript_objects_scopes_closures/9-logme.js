#!/usr/bin/node
let numArgs = 0;
exports.logMe = function (item) {
  const str = `${numArgs}: ${item}`
  console.log(str);
  numArgs++;
};
