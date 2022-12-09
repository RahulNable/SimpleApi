<template>
  <h1>hello 2</h1>
</template>

<script>
var xlsx = require("xlsx")
var fs = require('fs')
var dataPathExcelToRead = "Sample.xlsx"
var wb = xlsx.readFile(dataPathExcelToRead)
var sheetName = wb.SheetNames[0]
var sheetValue = wb.Sheets[sheetName]
var htmlData = xlsx.utils.sheet_to_html(sheetValue);
console.log(htmlData)

</script>