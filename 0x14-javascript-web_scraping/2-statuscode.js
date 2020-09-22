#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log('Error: ' + err);
  }
  console.log('code: ' + res.statusCode);
});
