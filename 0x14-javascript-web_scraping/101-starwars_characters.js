#!/usr/bin/node
/*
Prints all characters of a Star Wars movie by Movie ID.
*/

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characterUrls = JSON.parse(body).characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters (urls, index) {
  if (!urls || index >= urls.length) {
    return;
  }

  request(urls[index], (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharacters(urls, index + 1);
    }
  });
}
