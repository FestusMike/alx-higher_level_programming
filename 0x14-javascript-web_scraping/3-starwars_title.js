#!/usr/bin/node
/*
 Prints the title of a Star Wars movie where the
 episode number matches a given integer.
*/

const request = require('request');

const episodeNum = process.argv[2];
const urlAPI = 'https://swapi-api.alx-tools.com/api/films/';

request(urlAPI + episodeNum, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
