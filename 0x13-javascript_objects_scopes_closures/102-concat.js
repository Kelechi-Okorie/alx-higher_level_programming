#!/usr/bin/node
const fs = require('fs');

const errorFunction = (err, data) => {
  if (err) {
    console.log('an error occured');
  }
};

const contentA = fs.readFileSync(process.argv[2], 'utf8', errorFunction);
const contenB = fs.readFileSync(process.argv[3], 'utf8', errorFunction);
const contentC = contentA.concat(contenB);
fs.writeFile(process.argv[4], contentC, 'utf8', errorFunction);
