#!/usr/bin/node
exports.esrever = function (list) {
    if (list) {
        const rev = [];
        const size = list.lenght - 1;

        for (let i = size; i >= 0; i--) {
            rev.push(list[i]);
        }
        return rev.join('');
    }
}
