#!/usr/bin/node
// number of tasks completed by user id.

const req = require('request');

req.get(process.argv[2], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const tsksCompleted = {};
  body.forEach((data) => {
    if (data.completed) {
      if (!tsksCompleted[data.userId]) {
        tsksCompleted[data.userId] = 1;
      } else {
        tsksCompleted[data.userId] += 1;
      }
    }
  });
  console.log(tsksCompleted);
});
