#!/usr/bin/node
const args = [];
let i;
let max;
if (!process.argv[2]) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    args.push(Number(process.argv[i]));
  }
  max = Math.max.apply(null, args);
  args.splice(args.indexOf(max), 1);
  console.log(Math.max.apply(null, args));
}
