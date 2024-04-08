#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));
const msg1 = 'Missing number of occurrences';
const msg2 = 'C is fun';

if (isNaN(x)) {
  console.log(msg1);
} else {
  let i = x;
  while (i > 0) {
    console.log(msg2);
    i--;
  }
}
