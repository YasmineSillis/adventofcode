const input = require('./input.js');
console.log(input.length);

let array = input.split('\n');
let modifiedArray = array.map((pakjeAlsWoord) => {
    return pakjeAlsWoord.split('x');
});

const l = 0;
const w = 1;
const h = 2;

modifiedArray[0].sort();

function doIets(eerste, andere) {
    const resultaat = eerste - andere;
    console.log('we vergelijken nu ' + eerste + ' met' + andere + ', resultaat ' + resultaat);
    return resultaat;
}

const vgl = (a, b) => a - b;
console.log([1, 18, 9, 5, 4, 8].sort(vgl));

let huidigePositie = 0;
let totaalpapier = 0;
let totaalribbon = 0;

while (huidigePositie < modifiedArray.length) {
    let gesorteerdpakje = modifiedArray[huidigePositie].sort(vgl).map(Number);
    console.log(gesorteerdpakje);
    huidigePositie = huidigePositie + 1;
    let papier = 2 * gesorteerdpakje[l] * gesorteerdpakje[w] + 2 * gesorteerdpakje[w] * gesorteerdpakje[h] + 2 * gesorteerdpakje[h] * gesorteerdpakje[l] + gesorteerdpakje[l] * gesorteerdpakje[w];
    console.log(papier);
    totaalpapier = totaalpapier + papier;
    let ribbon = gesorteerdpakje[l] + gesorteerdpakje[l] + gesorteerdpakje[w] + gesorteerdpakje[w] + gesorteerdpakje[l] * gesorteerdpakje[w] * gesorteerdpakje[h];
    totaalribbon = totaalribbon + ribbon
}

console.log(totaalpapier);
console.log(totaalribbon);