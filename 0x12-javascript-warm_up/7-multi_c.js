#!/usr/bin/node

const argument = process.argv[2];

if (argument) {
  let number = parseInt(argument);

  if (!isNaN(number)) {
    while (number > 0) {
      console.log('C is fun');
      number--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
