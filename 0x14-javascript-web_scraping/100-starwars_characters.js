#!/usr/bin/node
/*
Prints all characters of a Star Wars movie by Movie ID.
*/

const request = require('request');

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(apiUrl, (err, result, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    const charUrls = movie.characters;

    function printName (urls) {
      if (urls.length === 0) {
        return;
      }

      const charUrl = urls.shift();
      request(charUrl, (err, result, body) => {
        if (err) {
          console.error(err);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
          printName(urls);
        }
      });
    }

    printName(charUrls);
  }
});
