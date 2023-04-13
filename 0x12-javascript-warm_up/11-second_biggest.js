#!/usr/bin/node
const MyInput = process.argv.slice(2).sort((a, b) => a - b);
if (!isNaN(MyInput[1])) {
  console.log(MyInput[MyInput.length - 2]);
} else {
  console.log('0');
}
