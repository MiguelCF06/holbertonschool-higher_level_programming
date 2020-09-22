#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const moviesList = JSON.parse(body).results;
    for (const idx in moviesList) {
      const characters = moviesList[idx].characters;
      for (const charIdx in characters) {
        if (characters[charIdx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
