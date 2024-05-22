#!/usr/bin/node
// Star wars Wedge Antilles
const req = require('request');
let number = 0;

req.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const cont = JSON.parse(body);
    cont.results.forEach((movie) => {
      movie.characters.forEach((char) => {
        if (char.includes(18)) {
          number += 1;
        }
      });
    });
    console.log(number);
  }
});
