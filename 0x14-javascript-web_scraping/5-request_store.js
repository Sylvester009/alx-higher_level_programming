#!/usr/bin/node
// Loripsum

const req = require('request');
const fileSystem = require('fs');

req.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    fileSystem.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
