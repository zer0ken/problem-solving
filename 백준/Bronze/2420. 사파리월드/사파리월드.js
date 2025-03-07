const input = require("fs").readFileSync(0, encoding = 'utf-8').toString().split(" ");
const [N, M] = input.map(Number);
console.log(Math.abs(N - M));