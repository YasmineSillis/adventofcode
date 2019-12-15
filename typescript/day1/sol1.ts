import { input } from "./input";

console.log(input.length);

 const newInput = input.split("\n")
 console.log(input.split("\n"))

 console.log(newInput[0])

 const  pakjes= newInput.map(el => {
     return el.split("x").map(el=>{return Number(el)}).sort((a,b)=> {return a-b})
    });
 console.log(pakjes);
 
const l = 0
const w = 1
const h = 2

let index = 0
let totaalpapier = 0
while(index < pakjes.length){
    let gesorteerdPakje = pakjes[index];
    let papier = 2*gesorteerdPakje[l]*gesorteerdPakje[w]+2*gesorteerdPakje[w]*gesorteerdPakje[h] + 2*gesorteerdPakje[l]*gesorteerdPakje[h] + gesorteerdPakje[l]*gesorteerdPakje[w]
    index = index + 1
    totaalpapier = totaalpapier + papier
}

console.log(totaalpapier);

index = 0
let totaalRibbon = 0
while(index < pakjes.length){
    let gesorteerdPakje = pakjes[index]
    let ribbon = 2*gesorteerdPakje[l] + 2*gesorteerdPakje[w] + 1*gesorteerdPakje[l]*gesorteerdPakje[w]*gesorteerdPakje[h]
    index = index + 1
    totaalRibbon = totaalRibbon + ribbon
}

console.log(totaalRibbon);
