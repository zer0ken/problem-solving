const year = parseInt(require("fs").readFileSync(0, encoding = 'utf-8').toString());
console.log((year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ? "1" : "0");