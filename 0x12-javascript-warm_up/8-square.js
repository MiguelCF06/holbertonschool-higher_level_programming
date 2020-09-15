#!/usr/bin/node
let i;
const arg = Number(process.argv[2]);

if (!arg) {
  console.log('Missing size');
} else {
  for (i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
