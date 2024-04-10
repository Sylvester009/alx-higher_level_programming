#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (counts, curr) {
    return curr === searchElement ? counts + 1 : counts
  }, 0)
}
