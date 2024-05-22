#!/usr/bin/node
// Star wars movie title

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
