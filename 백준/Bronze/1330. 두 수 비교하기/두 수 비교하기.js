const input = require("fs").readFileSync(0, encoding='utf-8').toString().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

if (a == b) {
    console.log("==");
} else if (a < b) {
    console.log("<");
} else {
    console.log(">");
}