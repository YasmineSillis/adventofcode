const md5 = require('pure-md5').md5;

const input = "bgvyzdsv";
let currNb = 0;
while (!md5(input + currNb++).startsWith('000000')) {
}
console.log(currNb);
