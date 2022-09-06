#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return result;
}

const result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(result);
