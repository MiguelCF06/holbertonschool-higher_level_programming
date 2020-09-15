#!/usr/bin/node
const number = process.argv[2];
if (!number) {
  console.log('Not a number');
} else if (!Number(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(number));
}
