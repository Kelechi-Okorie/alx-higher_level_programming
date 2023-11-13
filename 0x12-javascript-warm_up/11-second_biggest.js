#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(num => Number.parseInt(num));
  const sorted = list.sort((a, b) => b - a);
  console.log(sorted[1]);
}
