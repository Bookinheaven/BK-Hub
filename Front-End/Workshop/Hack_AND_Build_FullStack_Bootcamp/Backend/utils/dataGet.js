const xlsx = require("xlsx");
const path = require("path")
    
function getData(){
    let filePath = path.resolve(__dirname, "../../Data/Data.xlsx");
    let workbook = xlsx.readFile(filePath);
    let sheetName = workbook.SheetNames[0]; 
    let sheet = workbook.Sheets[sheetName];
    return xlsx.utils.sheet_to_json(sheet);

}