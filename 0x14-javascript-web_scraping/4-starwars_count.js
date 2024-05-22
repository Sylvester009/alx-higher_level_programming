#!/usr/bin/node
// Star wars Wedge Antilles
const req = require('request');
let number = 0;


req.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const cont = JSON.parse(body);
    cont.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          number += 1;
        }
      });
    });
    console.log(number);
  }
});
