#!/usr/bin/node

const process = require('node:process');
const arg = process.argv[2];
const number = parseInt(arg);
const message = !isNaN(number) ? `My number: ${number}` : 'Not a number';

console.log(message);
