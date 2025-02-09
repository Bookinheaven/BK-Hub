

function CelsiusToFaharenheit(cel){
    if (cel != 0){
        return cel * 9.0 /5.0 + 32.0
    } else return 0
}
console.log(CelsiusToFaharenheit(10) + " F")


const lamda = (cel) => {
    return `Celsius: ${cel} C\nFaharenheit: ${(cel * 9.0/5.0 + 32)} F`
}
console.log(lamda(10))