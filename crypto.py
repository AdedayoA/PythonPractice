import urllib.request 
import json
import locale

locale.setlocale( locale.LC_ALL, '' )
locale.currency( 1234.50, grouping = True )

def printResults(data):
  print('\nLocale from environment:', locale.getlocale())
  theJSON = json.loads(data)
  print("Last Price: " + theJSON["last"]
    + "\nLast 24 hours price high: " + theJSON["high"]
    + "\nast 24 hours price low " + theJSON["low"]
    + "\nLast 24 hours volume weighted average price: " + theJSON["vwap"]
    + "\nLast 24 hours volume: " + theJSON["volume"]
    + "\nHighest buy order " + theJSON["bid"]
    + "\nLowest sell order: " + theJSON["ask"]
    + "\nUnix timestamp date and time: " + theJSON["timestamp"]
    + "\nFirst price of the day: " + theJSON["open"])
  print('\nLocale from environment:', locale.getlocale())

def user_input_currency():
  currency = ["btcusd", "btceur", "eurusd", "xrpusd", "xrpeur", "xrpbtc", "ltcusd", "ltceur", "ltcbtc", "ethusd", "etheur", "ethbtc", "bchusd", "bcheur", "bchbtc"]
  user_input = input("What magnitude of earthquakes would you like to view:\n1) BTCUSD\n2) BTCEUR \n3) EURUSD\n4) XRPUSD \n5) XRPEUR\n6) XRPBTC \n7) LTCUSD \n8) LTCEUR\n9) LTCBTC \n10) ETHUSD\n11) ETHEUR \n12) ETHBTC\n13) BCHUSD \n14) BCHEUR\n15) BCHBTC\n")
  if user_input in currency:
    print ("Found it")
  if user_input not in currency:
    print ("Did not find it")
    user_input = currency[0]
  return user_input


def main():
  currency_pair = user_input_currency()
  urlData = "https://www.bitstamp.net/api/v2/ticker/" + currency_pair

    # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    data = data.decode("utf-8") # in Python 3.x we need to explicitly decode the response to a string
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
  main()