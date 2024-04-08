#!/usr/bin/node

const process = require('node:process');

const argCount = process.argv.length - 2;
const message = argCount === 1 ? 'Argument found' : argtCount < 1 ? 'No argument' : 'Arguments found';

console.log(message);
