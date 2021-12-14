#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    list.reduce(a, v => (v === searchElement ? a + 1 : a), 0);
}
