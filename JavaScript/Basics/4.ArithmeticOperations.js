// Perform basic arithmetic operations (+, -, *, /, %).


function add(...args) {
    let sum = 0
    for (let arg of args){
        sum += arg
    }
    return sum
}

function sub(...args) {
    let sub = args[0]
    for (let arg in args){
        if (arg > 0) {
            sub -= args[arg]
        }
    }
    return sub
}

function mult(...args) {
    let mul = 1
    for (let arg of args){
        mul *= arg
    }
    return mul
}

function div(a,b) {
    if(a > 0 && b > 0){
        return a / b
    } else if (a == 0) {
        return "Not possible"
    }
}

function mod(a,b) {
    return a % b
    
}

console.log(add(1,2,3,4,5))
console.log(sub(15,2,3,4,5))
console.log(mult(1,2,3,4,5))
console.log(div(5,10))
console.log(mod(5,10))
