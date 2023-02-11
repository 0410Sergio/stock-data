$Time = Get-Date -Format "HH:mm:ss"
$Location = Get-Location
#$stockArray = @('AAPL','AMGN','AXP','BA','CAT','CRM','CSCO','CVX','DIS','DOW','GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT','NKE','PG','TRV','UNH','V','VZ','WBA','WMT')
$stockArray = @('AAPL')
$temp = ''
$stockPrice = ''

$Time = Get-Date -Format "HH:mm:ss"
# Gets stock data and pushes it to database
foreach ($element in $stockArray) {
    Clear-Content .\$element-stock.json
    Write-Output( node .\GetStockInfo.js $element >> .\$element-stock.json)

    $temp = Get-Content .\$element-stock.json -Raw | ConvertFrom-Json
    Clear-Content .\$element-stock.json

    $stockPrice = node .\ModifyStockInfo.js $element -Raw | ConvertFrom-Json

    #Write-Output($temp)

    $temp.historical += $stockPrice
    $temp = $temp | ConvertTo-Json

    Add-Content .\$element-stock.json $temp
    Start-Sleep -Second 2 

    Write-Output( python CommitStockData.py $element)
    Start-Sleep -Second 2
}

# Gets news data and pushes it to database
#if($Time -eq '09:35:00'){}
foreach ($element in $stockArray) {
    Clear-Content .\$element-news.json
    Write-Output( node .\GetNewsInfo.js $element >> .\$element-news.json)

    $temp = Get-Content .\$element-news.json -Raw
    Clear-Content .\$element-news.json

    Add-Content .\$element-news.json $temp | ConvertTo-Json
    Start-Sleep -Second 2 

    Write-Output( python CommitNewsData.py $element)
    Start-Sleep -Second 2
}

Write-Output($Time)


