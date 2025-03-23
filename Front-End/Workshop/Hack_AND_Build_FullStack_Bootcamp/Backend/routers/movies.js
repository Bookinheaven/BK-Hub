const express = require("express");
const router = express.Router();
const xlsx = require("xlsx");
const path = require("path");

function getData(file) {
    try {
        let filePath = path.resolve(__dirname, `../../Data/${file}.xlsx`);
        let workbook = xlsx.readFile(filePath);
        let sheetName = workbook.SheetNames[0]; 
        let sheet = workbook.Sheets[sheetName];
        return xlsx.utils.sheet_to_json(sheet);
    } catch (error) {
        console.error(`Error reading file ${file}.xlsx:`, error);
        return [];
    }
}

router.get("/data/:type", (req, res) => {    
    let data = [];
    
    if (req.params.type === "recommendations") {
        data = getData("Recent");
    } else if (req.params.type === "suggestions") {
        data = getData("rec");
    } else {
        return res.status(400).json({ message: "Invalid request type." });
    }

    return res.json({ Data: data });
});

module.exports = router;
