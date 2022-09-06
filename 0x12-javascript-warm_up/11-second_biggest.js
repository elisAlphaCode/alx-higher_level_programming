#!/usr/bin/node

const inputs = process.argv.slice(2);

if (!inputs.length || inputs.length === 1) {
  console.log(0);
} else {
  const num = inputs.map(input => parseInt(input));
  console.log(num.sort()[num.length - 2]);
}
