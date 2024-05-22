#!/usr/bin/node

const fileSystem = require('fs');

fileSystem.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (error) {
    if (error) {
      console.log(err);
    }
  });
