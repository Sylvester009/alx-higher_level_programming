#!/usr/bin/node
// Reads & prints content of a file.

const fileSystem = require('fs');
fileSystem.readFile(process.argv[2], 'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
