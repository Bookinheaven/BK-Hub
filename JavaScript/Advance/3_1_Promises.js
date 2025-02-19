function watchPromises() {
    return new Promise((resolve, reject) => {
        if(userLeft) {
            reject({
                name: "User left",
                message: ":("
            })
        } else if(userWatchingCatMeme) {
            reject({
                name: "User watching",
                message: " :D "
            })
        } else {
            resolve("NO not now")
        }
    })   
}


watchPromises().then( (message) => {
    console.log("Success " + message)
}).catch((error) => {
    console.log(error.name, " " + error.message)
})
