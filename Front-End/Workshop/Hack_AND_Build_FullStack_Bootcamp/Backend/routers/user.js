const express = require("express")

const router = express.Router();

router.get("data:username", (req, res) => {
    console.log(req.params)
})

module.exports = router