#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

const callback = (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let count = 0;

    for (let i = 0; i < results.length; i++) {
      const result = results[i];
      const characters = result.characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  }
};

request(url, callback);
