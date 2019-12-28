import {input} from "./input"

console.log(input.length);

let xSanta = 0
let ySanta = 0
let xRobot = 0
let yRobot = 0
let indexSanta = 0
let indexRobot = 1
let list = []
while(indexRobot < input.length){
    if (input.charAt(indexSanta) == "^"){
        ySanta = ySanta + 1
    }
    if (input.charAt(indexSanta) == "v"){
        ySanta = ySanta - 1
    }
    if (input.charAt(indexSanta) == ">"){
        xSanta = xSanta + 1
    }
    if (input.charAt(indexSanta) == "<"){
        xSanta = xSanta - 1
    }
    if (input.charAt(indexRobot) == "^"){
        yRobot = yRobot + 1
    }
    if (input.charAt(indexRobot) == "v"){
        yRobot = yRobot - 1
    }
    if (input.charAt(indexRobot) == ">"){
        xRobot = xRobot + 1
    }
    if (input.charAt(indexRobot) == "<"){
        xRobot = xRobot - 1
    }
    let coordinaatSanta = "c" + xSanta + "r" + ySanta
    if (list.indexOf(coordinaatSanta) == -1){
        list.push(coordinaatSanta)
    }
    let coordinaatRobot = "c" + xRobot + "r" + yRobot
    if (list.indexOf(coordinaatRobot) == -1){
        list.push(coordinaatRobot)
    }
    indexSanta = indexSanta + 2
    indexRobot = indexRobot + 2
}

console.log(list.length);