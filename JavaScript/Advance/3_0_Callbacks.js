const userLeft = false 
const userWatchingCatMeme = false

function watchCallback(callback, errorCallback) {
    if(userLeft) {
        errorCallback({
            name: "User left",
            message: ":("
        })
    } else if(userWatchingCatMeme) {
        errorCallback({
            name: "User watching",
            message: " :D "
        })
    } else {
        callback("NO not now")
    }
}

watchCallback((message) => {
    console.log("Success " + message)
}, (error) => {
    console.log(error.name, " " + error.message)
})