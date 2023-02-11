
const process = require('process');
const https = require('https')

let stockPick = process.argv[2]
//let stockPick = 'AAPL'

const options = {
  hostname: 'financialmodelingprep.com',
  port: 443,
  path: '/api/v3/quote-short/' + stockPick + '?apikey=***************',
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
