#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newArray[j] = list[i];
    j++;
  }
  return newArray;
};
