#!/usr/bin/node
function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
let num = Number(process.argv[2]);
if (!num) {
  num = 0;
}
console.log(factorial(num));
