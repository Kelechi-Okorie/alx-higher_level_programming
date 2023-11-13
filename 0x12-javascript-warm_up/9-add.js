#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]));
