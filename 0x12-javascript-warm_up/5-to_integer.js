#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(num);
}
