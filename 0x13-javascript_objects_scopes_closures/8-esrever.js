#!/usr/bin/node

/*
function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  const reversedList = [];

  for (let j = list.length - 1; j >= 0; j--) {
    reversedList.push(list[j]);
  }

  return (reversedList);
};
