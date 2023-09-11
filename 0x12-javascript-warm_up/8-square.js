#!/usr/bin/node

const args = process.argv;

if (args.length === 2) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2]);

  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
