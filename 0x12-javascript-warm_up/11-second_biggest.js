#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length > 1) {
  const numbers = args.map(arg => parseInt(arg));
  numbers.sort((m, n) => m - n);
  console.log(numbers[numbers.length - 2]);
} else {
  console.log(0);
}
