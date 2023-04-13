#!/usr/bin/node
const dict = require('./101-data').dict;
const ListVal = Object.values(dict);
const ListValues = [...new Set(ListVal)];
const output = {};
for (const ActualVal in ListValues) {
  const arr = [];
  for (const key in dict) {
    if (dict[key] === ListValues[ActualVal]) {
      arr.push(key);
    }
  }
  output[ListValues[ActualVal]] = arr;
}
console.log(output);
