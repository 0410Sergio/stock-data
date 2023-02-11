
const process = require('process');
const https = require('https')

let currentDate = new Date();
let year = currentDate.getFullYear()
let month = (currentDate.getMonth()).toString()
let day = (currentDate.getDate()).toString()
if( day.split('').length === 1) {
  day = ('0' + day).toString()
}
if( month === '0') {
  month = '12'
  year = (Number(year) - 1).toString()
}
if( month.split('').length === 1) {
  month = ('0' + month).toString()
}
let formatDate = year + '-' + month + '-' + day
let stockPick = process.argv[2]
//let stockPick = 'AAPL'


const options = {
  hostname: 'financialmodelingprep.com',
  port: 443,
  path: '/api/v3/historical-price-full/' + stockPick + '?from=' + formatDate + '&apikey=********************',
  method: 'GET'
}

const req = https.request(options, (res) => {
  res.on('data', (d) => {
    process.stdout.write(d)
  })
}) 

req.on('error', (error) => {
  console.error(error)
})

req.end() 
