#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileToStore = process.argv[3];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileToStore, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
