const express = require("express")
const path = require("path")
const app = express(); 
const expressLayouts = require("express-ejs-layouts");
const indexRouter = require("./Backend/routers/index.js")
const movieRouter = require("./Backend/routers/movies.js")

app.set("view engine", "ejs");
app.use(expressLayouts)
app.set("views", path.join(__dirname, "Frontend", "views"))
app.use(express.static(path.join(__dirname, "Frontend", "public")))
app.set("layout", "layouts/layout");

app.use(express.urlencoded({ limit: "10gb", extended: false }));
app.use(express.json());

app.use("/", indexRouter)
app.use("/movie", movieRouter)
app.listen(3414, () => {
    console.log("Server: http://localhost:3414")
})
