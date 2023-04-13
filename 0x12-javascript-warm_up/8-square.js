#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const myVal = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < myVal; i++) {
    console.log('X'.repeat(myVal));
  }
} else {
  console.log('Missing size');
}
