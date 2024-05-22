#!/usr/bin/node
// Star wars Wedge Antilles
const req = require('request');
const url = process.argv[2]
let number = 0;


req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          number += 1;
        }
      });
    });
    console.log(number);
  }
});
