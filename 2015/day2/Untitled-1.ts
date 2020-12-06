import { input } from "./input";

const newInput = input.split("\n")
console.log(newInput);

const pakjes = newInput.map(el => el.split("x").map(el=>Number(el)).sort((a,b) => (a - b)))
console.log(pakjes);

const l = 0
const w = 1
const h = 2

let totaalPapier = 0
let index = 0
while(index < pakjes.length){
    let gesorteerdPakje = pakjes[index]
    let papier = 2*gesorteerdPakje[l]*gesorteerdPakje[w] + 2*gesorteerdPakje[w]*gesorteerdPakje[h] + 2*gesorteerdPakje[h]*gesorteerdPakje[l] + gesorteerdPakje[l]*gesorteerdPakje[w]
    totaalPapier = totaalPapier + papier
    index = index + 1
}

console.log(totaalPapier);

index = 0
let totaalRibbon = 0
while (index < pakjes.length){
    let gesorteerdPakje = pakjes[index]
    let ribbon = 2*gesorteerdPakje[l] + 2*gesorteerdPakje[w] + gesorteerdPakje[l]*gesorteerdPakje[w]*gesorteerdPakje[h]
    totaalRibbon = totaalRibbon + ribbon
    index = index + 1
}

console.log(totaalRibbon)