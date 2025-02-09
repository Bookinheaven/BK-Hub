// Build a simple grading system (e.g., if marks >= 90: grade A, else grade B, etc.).


function grades(marks) {

    if (marks >= 90) {
        return "A" 
    } 
    else if (marks >= 85) {
        return "B" 
    } 
    else if (marks >= 70) {
        return "C" 
    } 
    else if (marks >= 60) {
        return "D" 
    } 
    else if (marks < 60) {
        return "F" 
    } 
    else {
        return "idk"
    }
}

console.log(grades(99))
console.log(grades(85))
console.log(grades(76))
console.log(grades(66))
console.log(grades(41))