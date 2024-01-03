#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

const callback = (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    // const map = results.map((result, index) => {
    //   return results.characters;
    // });
    const filter = results.filter((result, index) => {
      const characters = result.characters;
      return characters.filter(character => character.includes('18')).length;
    });

    console.log(filter.length);
  }
};

request(url, callback);
