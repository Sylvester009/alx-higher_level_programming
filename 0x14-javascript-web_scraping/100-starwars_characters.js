#!/usr/bin/node

const req = require('request');
const identity = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${identity}`;

req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const chars = content.characters;
    for (const char of chars) {
      req.get(char, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else {
          const contNames = JSON.parse(body);
          console.log(contNames.name);
        }
      });
    }
  }
});
