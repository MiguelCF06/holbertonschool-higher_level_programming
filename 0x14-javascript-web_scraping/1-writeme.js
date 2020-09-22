#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const stringToWrite = process.argv[3];
fs.writeFile(fileName, stringToWrite, function (err) {
  if (err) {
    console.log(err);
  }
});
