#!/usr/bin/node
let firstArg = process.argv[2];
let secondArg = process.argv[3];
if (!firstArg) {
  firstArg = 'undefined';
} else if (!secondArg) {
  secondArg = 'undefined';
}
console.log(firstArg + ' is ' + secondArg);
