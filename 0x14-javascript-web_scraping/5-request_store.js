#!/usr/bin/node
/*
Gets the contents of a webpage and stores it in a file.
*/

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
      }
    });
  }
});
