#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const sortArgs = args.sort((a, b) => a - b);
  console.log(sortArgs[sortArgs.length - 2]);
}
