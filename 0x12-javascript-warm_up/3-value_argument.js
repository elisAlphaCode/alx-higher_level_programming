#!/usr/bin/node

const passedArg = process.argv[2];

if (passedArg) {
  console.log(passedArg);
} else {
  console.log('No argument');
}
