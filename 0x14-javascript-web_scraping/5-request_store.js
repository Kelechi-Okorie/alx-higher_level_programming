#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    try {
      fs.writeFile(filename, body, 'utf-8', (err, result) => {
        if (err) {
          console.log(err);
        }
      });
    } catch (err) {
      console.log(err);
    }
  }
});
