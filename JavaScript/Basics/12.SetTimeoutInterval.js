setTimeout(()=> {
    console.log("Fun is called")
}, 3000)

let x = 0
setInterval(()=> {
    console.log("Fun is called "+ x++)
}, 3000)