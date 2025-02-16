const recordVideoOne = new Promise((resolve, reject) => {
    resolve("Video one recorded")
})

const recordVideoTwo = new Promise((resolve, reject) => {
    resolve("Video Tqo recorded")
})
const recordVideoThree = new Promise((resolve, reject) => {
    resolve("Video Three recorded")
})

//returns all because it waits until everything is completes 
Promise.all([
    recordVideoOne,
    recordVideoTwo,
    recordVideoThree
]).then((messages) => {
    console.log(messages)
})

//returns only one since it post only promise which completes first
Promise.race([
    recordVideoOne,
    recordVideoTwo,
    recordVideoThree
]).then((message) => {
    console.log(message)
})