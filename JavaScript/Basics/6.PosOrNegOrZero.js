// Write a program to check if a number is positive, negative, or zero.

function check (number) {
    if (number < 0) {
        return "Negative"
    } else if (number > 0) {
        return "Positive"
    } if (number == 0) {
        return "Zero"
    }
}

console.log(check(0))
console.log(check(10))
console.log(check(-10))
