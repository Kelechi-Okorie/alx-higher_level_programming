#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
const content = process.argv[3];

try {
  fs.writeFile(filename, content, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
