#!/usr/bin/node

const argument = process.argv[2];
let output = 'Not a number';

if (argument) {
  const number = parseInt(argument);

  if (!isNaN(number)) {
    output = `My number: ${number}`;
  }
}

console.log(output);
