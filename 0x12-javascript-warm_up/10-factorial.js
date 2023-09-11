#!/usr/bin/node

const args = process.argv;

if (args.length > 2) {
  const number = parseInt(args[2]);

  if (isNaN(number)) {
    console.log(1);
  } else {
    const f = factorial(number);
    console.log(f);
  }
} else {
  console.log(1);
}

function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
