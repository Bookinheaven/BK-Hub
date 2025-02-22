function makeRequest(location) {
    return new Promise((resolve, reject) => {
        console.log(`Making request to ${location}`)
        if (location == 'Google') {
            resolve('Google says hi')
        } else {
            reject('We can only talk to google')
        }
    })
}

function processRequest(response) {
    return new Promise((resolve, request) => {
        console.log('Processing response')
        resolve(`Extra Information + ${response}`)
    })
}

// const newLocal = makeRequest('Google').then((response) => {
//     console.log(response)
//     return processRequest(response)
// }).then(processedResponse => {
//     console.log(processedResponse)
// }).catch(err => {
//     console.log(err)
// })

async function doWork() {
    try {
        const response = await makeRequest('Google')
        console.log('Response Recesived')
        const processResponse = await processRequest(response) 
        console.log(processResponse)
    } catch(err) {
        console.log(err)
    }
}
doWork()