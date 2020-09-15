#!/usr/bin/node
const myVar = process.argv[2];
if (!myVar) {
  console.log('No argument');
} else {
  console.log(myVar);
}
