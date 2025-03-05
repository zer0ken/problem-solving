const stdin = process.platform === "linux" ? "/dev/stdin" : "테스트/input.txt";
const input = require("fs").readFileSync(stdin).toString().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

console.log(a + b);
