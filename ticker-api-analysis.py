#install "requests" using pip install requests
#install "JSON" using pip install json
#this api displays cryptocurrency ticker data in order of rank. The maximum number of results per call is 100.
#Pagination is possible by using the start and limit parameters.
import json#importing the libraries
import requests#importing the libraries

while True:

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array' #getting the api link

    limit = 100#initialising the parameters
    start = 1
    sort = 'rank'
    convert = 'USD'

    choice = input("Do you want to enter any custom parameters? (y/n): ") # we can add our own parameters

    if choice == 'y': # if we select our own parameters
        limit = input('What is the custom limit?: ')
        start = input('What is the custom start number?: ')
        sort = input('What do you want to sort by?: ')
        convert = input('What is your local currency?: ')

    ticker_url += '&limit=' + str(limit) + '&sort=' + sort + '&start=' + str(start) + '&convert=' + convert# add the things to th eurl

    request = requests.get(ticker_url) #getting the url and parsing it to JSON
    results = request.json()

    print(json.dumps(results, sort_keys=True, indent=4))

    data = results['data'] #sending data to a variable

    print()
    for currency in data: #printing all the required data
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])

        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume) #formating it into strings
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)

        print(str(rank) + ': ' + name + ' (' + symbol + ')') #formating the outputs
        print('Market cap: \t\t$' + market_cap_string)
        print('Price: \t\t\t$' + str(price))
        print('24h Volume: \t\t$' + volume_string)
        print('Hour change: \t\t' + str(hour_change) + '%')
        print('Day change: \t\t' + str(day_change) + '%')
        print('Week change: \t\t' + str(week_change) + '%')
        print('Total supply: \t\t' + total_supply_string)
        print('Circulating supply: \t' + circulating_supply_string)
        print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
        print()

    choice = input('Again? (y/n): ') # Again asking for a choice

    if choice == 'n': #if no, break from the loop
        break
