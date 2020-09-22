#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.title);
});
