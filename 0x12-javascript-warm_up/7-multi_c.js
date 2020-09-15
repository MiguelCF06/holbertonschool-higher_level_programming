#!/usr/bin/node
const x = Number(process.argv[2]);
let i;
if (!x) {
  console.log('Missing number of occurrences');
}
for (i = 0; i < x; i++) {
  console.log('C is fun');
}
