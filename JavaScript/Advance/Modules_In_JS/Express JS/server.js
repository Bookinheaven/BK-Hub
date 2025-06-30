const express = require('express')
const UserRouter = require('./routers/users')
const app = express()

app.set("view engine", "ejs")
app.use(express.static("public"))
app.use(express.urlencoded({extended: true}))
// app.use(logger)
app.get('/', logger, (req, res, next) => {
// app.get('/', (req, res, next) => {
  console.log("Here")
  // res.send("Hi")
  // res.json({mess : "ASD"})
  // res.render("index", {text: "World"})
})
app.listen(3000)

function logger(req, res, next) {
  console.log(req.originalUrl)
  next()
}
app.use("/users", UserRouter)