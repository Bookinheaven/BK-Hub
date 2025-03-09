const express = require("express")
const router = express.Router()

router.get("/", (req, res) => {
    console.log(req.query.name)
    console.log(users)
    res.send("User List")
})
router.get("/new", (req, res) => {
    res.render("users/new", {firstName : "Burn"})
    // res.send("User new form")
})
router.post("/",  (req, res) => {
    // res.send("create user")
    // console.log(req.body.firstName) // to access body we have to use urluncoded() middleware
    // res.send("Hi")
    const isValid = true
    if (isValid) {
        users.push({ firstName: req.body.firstName})
        res.redirect(`/users/${users.length - 1}`)
    } else {
        console.log("Error")
        res.render("users/new", {firstName: req.body.firstName})
    }
})

router.route("/:id")
.get((req, res)=> {
    console.log(req.user)
    res.send(`Get User ${req.params.id}`)
    })
.put((req, res)=> {
    res.send(`Update User ${req.params.id}`)
    })
.delete((req, res)=> {
    res.send(`Delete User ${req.params.id}`)
    })
// router.get("/:id", (req, res) => {
//     res.send(`Get User ${req.params.id}`)
// })
// router.put("/:id", (req, res) => {
//     res.send(`Update User ${req.params.id}`)
// })
// router.delete("/:id", (req, res) => {
//     res.send(`Delete User ${req.params.id}`)
// })


// a type of middleware
const users = [{name: "Burn"}, {name: "Burn1"}, {name: "Bur2"}]
router.param("id", (req, res, next, id) => {
    console.log(id)
    req.user = users[id]
    next()
})
module.exports = router