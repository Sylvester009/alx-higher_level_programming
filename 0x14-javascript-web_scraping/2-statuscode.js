#!/usr/bin/node
// Status code of a GET request.

const req = require('request');
req.get(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
