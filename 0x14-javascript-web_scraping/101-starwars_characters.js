#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, index) {
  request.get(characters[index], (err, resp, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
