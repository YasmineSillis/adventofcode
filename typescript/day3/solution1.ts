import { input } from "./input"

console.log(input.length);

let x=0
let y=0
let index = 0
let list = []
while(index < input.length){
    if (input.charAt(index) == "^"){
        y = y + 1
    }
    if (input.charAt(index) == "v"){
        y = y - 1
    }
    if (input.charAt(index) == ">"){
        x = x + 1
    }
    if (input.charAt(index) == "<"){
        x = x - 1
    }
    let coordinaat = "c" + x + "r" + y
    if (list.indexOf(coordinaat) == -1){
        list.push(coordinaat)
    }
    index = index + 1
}

console.log(list.length);
