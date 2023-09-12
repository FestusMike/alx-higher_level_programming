#!/usr/bin/node

/*
Function returns number of occurrences in a list
*/

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((occurence) => {
    if (occurence === searchElement) count++;
  });
  return count;
};
