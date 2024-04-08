#!/usr/bin/node

const length = Math.floor(Number(process.argv[2]));
if (isNaN(length)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    let row = '';
    for (let j = 0; j < length; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
