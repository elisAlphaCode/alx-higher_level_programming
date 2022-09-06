#!/usr/bin/node

const square = process.argv[2];
const xSquare = 'X';

if (isNaN(square)) {
  console.log('Missing size');
} else {
  let counter = 1;

  while (counter <= square) {
    console.log(xSquare.repeat(square));
    counter++;
  }
}
