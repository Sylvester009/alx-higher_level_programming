#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  } else {
    console.log(error);
  }
});

function printChars (characters, index) {
  if (index >= characters.length) return;

  request.get(characters[index], (err, resp, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      printChars(characters, index + 1);
    } else {
      console.log(err);
    }
  });
}
