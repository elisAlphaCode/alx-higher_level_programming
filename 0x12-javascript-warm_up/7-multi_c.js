#!/usr/bin/node

const args = process.argv[2];

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  let counter = 1;

  while (counter <= args) {
    console.log('C is fun');
    counter++;
  }
}
