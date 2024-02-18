#!/usr/bin/node
/*
Prints the number of movies where the character
“Wedge Antilles” is present.
*/

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    if (data.results) {
      for (let i = 0; i < data.results.length; i++) {
        const characters = data.results[i].characters;
        for (let j = 0; j < characters.length; j++) {
          if (characters[j].includes('/18/')) {
            count += 1;
          }
        }
      }
      console.log(count);
    }
  }
});
