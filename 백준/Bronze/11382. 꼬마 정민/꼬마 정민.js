const input = require("fs").readFileSync("/dev/stdin").toString().split(' ');

const a = parseInt(input[0]);
const b = parseInt(input[1]);
const c = parseInt(input[2]);

console.log(a + b + c);
