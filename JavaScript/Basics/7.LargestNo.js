// Create a program to find the largest of three numbers.

function check(...args) {
    let largest = args[0]
    for (let arg in args) {
        if (args[arg] > largest){
            largest = args[arg]
        }
    }
    return largest
}

console.log(check(31,76,98))