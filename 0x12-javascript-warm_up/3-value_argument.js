#!/usr/bin/node

let arg;
if (process.argv[2]) {
  arg = process.argv[2];
} else {
  arg = 'No argument';
}

console.log(arg);
