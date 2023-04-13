#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((element, i) => list[list.length - i - 1]);
};
