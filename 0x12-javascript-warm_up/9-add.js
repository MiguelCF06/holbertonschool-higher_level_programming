#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (!a) {
  console.log('NaN');
} else if (!b) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
