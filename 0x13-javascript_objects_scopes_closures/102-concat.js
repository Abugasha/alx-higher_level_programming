#!/usr/bin/node
const fs = require('fs');
const MyFiles = process.argv.slice(2);
fs.readFile(MyFiles[0], 'utf8', function (err, data1) {
  if (err) console.log('error', err);
  fs.readFile(MyFiles[1], 'utf8', function (err, data2) {
    if (err) console.log('error', err);
    fs.writeFile(MyFiles[2], data1 + data2, function (err, result) {
      if (err) console.log('error', err);
    });
  });
});
