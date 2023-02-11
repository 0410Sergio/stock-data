
const process = require('process');
const https = require('https')

let stockPick = process.argv[2]


const options = {
  hostname: 'financialmodelingprep.com',
  port: 443,
  path: '/api/v3/stock_news?tickers=' + stockPick + '&limit=5&apikey=*********************',
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
