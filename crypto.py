import urllib.request, json, datetime, os, time, sys
from money.money import Money
from money.currency import Currency
from progress.bar import ShadyBar
def progress_bar():
  bar = ShadyBar('Processing', max=100)
  for i in range(100):
    bar.next()
    time.sleep(.025)
  bar.finish()

##Returns the jSON returned from webpage and prints out the data in US currency, but can be switched by changing the locale.
def printResults(data):
  theJSON = json.loads(data)
  progress_bar()
  print("Last Price: " + Money("{:.2f}".format(float(theJSON["last"])), Currency.USD).format('en_US')
    + "\nLast 24 hours price high: " + Money("{:.2f}".format(float(theJSON["high"])), Currency.USD).format('en_US')
    + "\nLast 24 hours price low " + Money("{:.2f}".format(float(theJSON["low"])), Currency.USD).format('en_US')
    + "\nLast 24 hours volume weighted average price: " + Money("{:.2f}".format(float(theJSON["vwap"])), Currency.USD).format('en_US')
    + "\nLast 24 hours volume: " + "{:,}".format(float(theJSON["volume"]))
    + "\nHighest buy order " + Money("{:.2f}".format(float(theJSON["bid"])), Currency.USD).format('en_US')
    + "\nLowest sell order: " + Money("{:.2f}".format(float(theJSON["ask"])), Currency.USD).format('en_US')
    + "\nLast Updated: " + datetime.datetime.fromtimestamp(int(theJSON["timestamp"])).strftime('%A, %d %B %Y %I:%M%p') 
    + "\nFirst price of the day: " + Money("{:.2f}".format(float(theJSON["open"])), Currency.USD).format('en_US'))

##Returns the crypto/currency the user picks
def user_input_currency():
  search = False 
  while (search != True):
    currency = ["btcusd", "btceur", "eurusd", "xrpusd", "xrpeur", "xrpbtc", "ltcusd", "ltceur", "ltcbtc", "ethusd", "etheur", "ethbtc", "bchusd", "bcheur", "bchbtc"] 

    user_input = input("Which crypto currency would you like more information on?:\n1) BTCUSD\n2) BTCEUR \n3) EURUSD\n4) XRPUSD \n5) XRPEUR\n6) XRPBTC \n7) LTCUSD \n8) LTCEUR\n9) LTCBTC \n10) ETHUSD\n11) ETHEUR \n12) ETHBTC\n13) BCHUSD \n14) BCHEUR\n15) BCHBTC\n").lower()

    if user_input in currency:
      os.system('clear')
      print ("Found it, information on " + user_input)
      search = True

    if user_input not in currency:
      print ("Did not find it")
      search = False

  return user_input

def main():
  currency_pair = user_input_currency()
  urlData = "https://www.bitstamp.net/api/v2/ticker/" + currency_pair

    # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  
  if (webUrl.getcode() == 400):
    print("The request with the provided information was invalid or cannot be retrieved.")
  elif (webUrl.getcode() == 404):
    print("The page no longer exists, not data to retrieve")
  elif (webUrl.getcode() == 200):
    print("Success!")
    data = webUrl.read()
    data = data.decode("utf-8")
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
  main()