const fs = require('fs')

function readFile(file="test.txt"){
    fs.readFile(file, 'utf8', function (err, data) {
        console.log(data)
    })
}
function writeFile(file="test1.txt", data="Testing 123"){
    fs.writeFile(file, data, function (err) {
        console.log("Data saved")
    })
}

function appendFile(file="test1.txt", data="\nTesting 422"){
    fs.appendFile(file, data, function (err) {
        console.log("Data saved")
    })
}

function deleteFile(file="test1.txt") {
    fs.unlink(file, function(err) {
        console.log("Deleted File")
    })
}

function createDir(folder="test"){
    fs.mkdir(folder, function(){
        console.log("Folder Created")
    })
}

function readDir(folder="test"){
    fs.readdir(folder, (err, content)=>{
        console.log(content)
    })
}
function checkStatForFile(file="test.txt"){
    fs.stat(file, (err, stat)=> {
        console.log(stat)
    })
}
function checkStatForFolder(folder="test"){
    fs.stat(folder, (err, stat)=> {
        console.log(stat)
        console.log(stat.isFile())
        console.log(stat.isDirectory())
    })
}

// readFile()
// writeFile()
// appendFile()
// deleteFile()
// createDir()
// readDir()
// checkStatForFile()
// checkStatForFolder()